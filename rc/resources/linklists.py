import inspect
from linkcheck import Linklist
from rc.resources.models import ResourceItem
from rc.resources.apps.operations import models as opts_models
from rc.resources.apps.education import models as edu_models
from rc.resources.apps.pae import models as pae_models

linklists = {}

def register_linklist_model(model_class):
    opts = model_class._meta
    class _ModelLinklist(Linklist):
        model = model_class
        object_filter = {}
        url_fields = ['url',]
    linklists.update({opts.verbose_name: _ModelLinklist})


model_classes = [ cls for name, cls in inspect.getmembers(pae_models) if inspect.isclass(cls) and
                  issubclass(cls, ResourceItem) and not (cls == ResourceItem)]
model_classes.extend([ cls for name, cls in inspect.getmembers(edu_models) if inspect.isclass(cls) and
                       issubclass(cls, ResourceItem) and not (cls == ResourceItem)])
model_classes.extend([ cls for name, cls in inspect.getmembers(opts_models) if inspect.isclass(cls) and
                       issubclass(cls, ResourceItem) and not (cls == ResourceItem)])

for klass in model_classes:
    register_linklist_model(klass)
