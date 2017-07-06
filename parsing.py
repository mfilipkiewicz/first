

import re
message = """@Title: End of the world
@Event Type: Natural disaster
@Date: 21-12-2012
@Details: World is going to end
@Others: All participants are asked to stay calm and relax"""

message_pattern = re.compile('@Title: (.*)\n@Event Type: (.*)\n@Date: (.*)\n@Details: (.*)\n@Others: (.*)')
title, event_type, date, details, others = message_pattern.search(message).groups()
print(title, '\n', event_type, '\n', date, '\n', details, '\n', others, '\n')