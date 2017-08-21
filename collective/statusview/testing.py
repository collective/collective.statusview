from plone import api
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_ROLES
from plone.app.testing import setRoles
import collective.statusview


class AddOnLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    package = collective.statusview

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=self.package)

    def tearDownZope(self, app):
        pass

    def setUpPloneSite(self, portal):
        profile_id = '{}:default'.format(self.package.__name__)

        self.applyProfile(portal, profile_id)

        # Enable default workflow.
        wf_tool = api.portal.get_tool('portal_workflow')
        wf_tool.setDefaultChain('simple_publication_workflow')

        # Give manager role to test user.
        setRoles(portal, TEST_USER_ID, TEST_USER_ROLES + ['Manager'])


FIXTURE = AddOnLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='{}:Integration'.format(AddOnLayer.package.__name__)
)
