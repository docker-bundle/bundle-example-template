def __bundle_installed__(actions = []):
  print(
"""====================================
      Example Bundle Installed
===================================="""
)
  return True # true dismiss default installed message

def __bundle_message__(actions = []):
  print(
"""====================================
            Example Bundle
===================================="""
)
  return False # true dismiss default bundle message

def example1(args = []):
  print('Example1~', args)

def example2(args = []):
  print('Example2~', args)

#expose actions
actions = {
  'example1': {
    'action': example1, # action function
    'desc': 'example1 like this' # action description
  },
  'example2': {
    'action': example2, # action function
    'desc': 'example2 like this' # action description
  },

  # inner action handler
  '__bundle_message__': __bundle_message__,
  '__bundle_installed__': __bundle_installed__,
}