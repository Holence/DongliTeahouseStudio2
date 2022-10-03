from __future__ import annotations
from DTPySide import *

base=os.path.dirname(__file__)+"\\"

Language_Dict={
    "简体中文": (QLocale.Language.Chinese, base+"zh_CN.qm"),
    "繁體中文": (QLocale.Language.LiteraryChinese, base+"zh_TW.qm"),
    "English": (QLocale.Language.English, base+"en.qm"),
    "Русский": (QLocale.Language.Russian, base+"ru.qm"),
    "日本語": (QLocale.Language.Japanese, base+"ja.qm"),
    "Esperanto": (QLocale.Language.Esperanto, base+"eo.qm")
}

Country_Dict={
    "中国":QLocale.Country.China,
    "United Kingdom":QLocale.Country.UnitedKingdom,
    "United States":QLocale.Country.UnitedStates,
    "日本":QLocale.Country.Japan,
    "Россия":QLocale.Country.Russia,
    "World":QLocale.Country.World
}