"""
This unit test checks the sendmessage() API call to make sure it raises
the correct exceptions.
"""

#pragma repy
#pragma repy restrictions.twoports

try:
  sendmessage('127.0.0.1', 12345, "x", '8.8.4.4', 12346)
except AddressBindingError:
  pass
except Exception, e:
  log("wrong exception for binding to non-local ip",'\n')
  log(str(e),'\n')
else:
  log("shouldn't be able to bind to non-local ip",'\n')

try:
  sendmessage('127.0.0.1', 12345, "x", '8.8.4.4', 12347)
except ResourceForbiddenError:
  pass
except Exception, e:
  log("wrong exception for binding to restricted port",'\n')
  log(str(e),'\n')
else:
  log("shouldn't be able to bind to restricted port",'\n')

