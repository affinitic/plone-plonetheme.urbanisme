from plonetheme.urbanisme.tests.base import ThemeurbanismeTestCase as TestCase


class ThemeurbanismeTestCase(TestCase):

    def test_urbanisme_layers_available(self):
        self.failUnless('urbanisme_images' in self.portal.portal_skins)
        self.failUnless('urbanisme_styles' in self.portal.portal_skins)
        self.failUnless('urbanisme_templates' in self.portal.portal_skins)

    def test_urbanisme_skin_installed(self):
        self.skins = self.portal.portal_skins
        theme = self.skins.getDefaultSkin()
        self.failUnless(theme == 'urbanisme Theme', 'Default theme is %s' % theme)


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
