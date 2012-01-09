from Products.CMFCore.utils import getToolByName
portal_url = getToolByName(context, 'portal_url')
portal = portal_url.getPortalObject()
language_tool = getToolByName(context, 'portal_languages')
language = language_tool.getPreferredLanguage()
response = context.REQUEST.RESPONSE
response.redirect(portal.absolute_url() + '/' + language)