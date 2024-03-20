from tools import *
from src.configs import *
from src.data import *
from src.docs import *

used_list = []

docs_time_main()

data_characters_convert(data_characters_collect())
append_unique(used_list, docs_characters_main())

data_story_convert(data_story_collect())
append_unique(used_list, docs_story_main())

#print(used_list)

