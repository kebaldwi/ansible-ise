from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from urllib.parse import quote
from ansible_collections.cisco.ise.plugins.module_utils.ise import (
    ISESDK,
    ise_argument_spec,
)
from ansible_collections.cisco.ise.plugins.module_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = ise_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    fdqn=dict(type="str"),
    userName=dict(type="str"),
    password=dict(type="str"),
    administration=dict(type="dict"),
    generalSettings=dict(type="dict"),
    profileConfiguration=dict(type="dict"),
    hostname=dict(type="str"),
))

required_if = [
    ("state", "present", ("hostname"), True),
    ("state", "absent", ("hostname"), True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NodeDeployment(object):
    def __init__(self, params, ise):
        self.ise = ise
        self.new_object = dict(
            fdqn=params.get("fdqn"),
            user_name=params.get("userName"),
            password=params.get("password"),
            administration=params.get("administration"),
            general_settings=params.get("generalSettings"),
            profile_configuration=params.get("profileConfiguration"),
            hostname=params.get("hostname"),
        )

    def get_object_by_name(self, name):
        try:
            result = self.ise.exec(
                family="node_deployment",
                function="get_node_details",
                params={"name": quote(name)}
            ).response
        except Exception as e:
            result = None
        return result

    def get_object_by_id(self, id):
        # NOTICE: Does not have a get by id method or it is in another action
        result = None
        return result

    def exists(self):
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("id")
        name = self.new_object.get("name")
        if o_id:
            if self.get_object_by_id(o_id):
                id_exists = True
        if name:
            if self.get_object_by_name(name):
                name_exists = True
        if id_exists and name_exists:
            _id = self.get_object_by_name(name).get("id")
            if o_id != _id:
                raise InconsistentParameters("The 'id' and 'name' params don't refer to the same object")
        return id_exists or name_exists

    def create(self):
        result = self.ise.exec(
            family="node_deployment",
            function="register_node",
            params=self.new_object,
        ).response
        return result

    def update(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if not name:
            name_ = self.get_object_by_id(id).get("name")
            self.new_object.update(dict(name=name_))
        result = self.ise.exec(
            family="node_deployment",
            function="update_node",
            params=self.new_object
        ).response
        return result

    def delete(self):
        id = self.new_object.get("id")
        name = self.new_object.get("name")
        result = None
        if not name:
            name_ = self.get_object_by_id(id).get("name")
            self.new_object.update(dict(name=name_))
        result = self.ise.exec(
            family="node_deployment",
            function="delete_node",
            params=self.new_object
        ).response
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        ise = ISESDK(self._task.args)
        obj = NodeDeployment(self._task.args, ise)

        state = self._task.args.get("state")

        response = None

        if state == "present":
            if obj.exists():
                response = obj.update()
                ise.object_updated()
            else:
                response = obj.create()
                ise.object_created()

        elif state == "absent":
            if obj.exists():
                response = obj.delete()
                ise.object_deleted()
            else:
                ise.object_already_absent()

        self._result.update(dict(ise_response=response))
        self._result.update(ise.exit_json())
        return self._result
