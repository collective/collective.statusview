from ..interfaces import ISettings
from Products.Five.browser import BrowserView
from plone.app.registry.browser import controlpanel
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.z3cform import layout


class SettingsEditForm(controlpanel.RegistryEditForm):

    schema = ISettings
    label = u'Status View Settings'
    description = u'Configure what is returned by @@status.'


class StatusViewConfiglet(BrowserView):

    def __call__(self):
        view_factory = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
        view = view_factory(self.context, self.request)
        return view()
