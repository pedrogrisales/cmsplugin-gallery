from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import GalleryPluginModel


class GalleryPlugin(CMSPluginBase):
    model = GalleryPluginModel
    name = _("Gallery Plugin")
    render_template = "plugin_gallery/gallery.html"
    fieldsets = (
        (None, {
            'fields': ('album',),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
        	'object': instance,
        	'images':instance.images
        })
        return context


plugin_pool.register_plugin(GalleryPlugin)
