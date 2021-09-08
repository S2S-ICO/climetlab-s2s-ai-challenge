from functools import partial

from climetlab import Dataset

from climetlab_s2s_ai_challenge.info import Info


class S2sDataset(Dataset):
    name = None
    home_page = "-"
    licence = "https://apps.ecmwf.int/datasets/data/s2s/licence/"
    documentation = "-"
    citation = "-"

    terms_of_use = (
        "By downloading data from this dataset, you agree to the terms and conditions defined at "
        "https://apps.ecmwf.int/datasets/data/s2s/licence/. "
        "If you do not agree with such terms, do not download the data. "
    )


def add_attributes(f, from_class):
    for t in ["name", "home_page", "licence", "documentation", "citation", "terms_of_use"]:
        # for t in from_class.__dir__():
        # if t.startswith("__"):
        #     continue
        setattr(f, t, getattr(from_class, t))


def add_info(f, dataset, fctype):
    f._info = Info(dataset)
    f.get_all_reference_dates = partial(f._info._get_config, "alldates", fctype=fctype)
