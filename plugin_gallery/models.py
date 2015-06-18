from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from filer.fields.folder import FilerFolderField




class GalleryPluginModel(CMSPlugin):
    album = FilerFolderField(verbose_name=_('album'))

    @property
    def images(self):
        if not hasattr(self, '__images'):
            files = self.album.files
            self.__images = [f for f in files if f.file_type == 'Image']
            self.__images.sort()
        return self.__images

    @property
    def size(self):
        if self.width and self.height:
            return "%dx%d" % (self.width, self.height)
