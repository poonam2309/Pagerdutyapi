# Pagerdutyapi


*Parameter Values*
Parameter		Description
url		Required. The url of the request
data		Optional. A dictionary, list of tuples, bytes or a file object to send to the specified url
json		Optional. A JSON object to send to the specified url
files		Optional. A dictionary of files to send to the specified url
allow_redirects		Optional. A Boolean to enable/disable redirection.
Default True (allowing redirects)
auth		Optional. A tuple to enable a certain HTTP authentication.
Default None
cert		Optional. A String or Tuple specifying a cert file or key.
Default None
cookies		Optional. A dictionary of cookies to send to the specified url.
Default None
headers		Optional. A dictionary of HTTP headers to send to the specified url.
Default None
proxies		Optional. A dictionary of the protocol to the proxy url.
Default None
stream		Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
Default False
timeout		Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
Default None which means the request will continue until the connection is closed
verify	
Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
Default True



*Operators*
OPERATORS	DESCRIPTION
contains	The field contains a value.
ncontains	The field does not contain a value.
exists	The field exists.*Parameter Values*
*Parameter		Description
*url		Required. The url of the request
*data		Optional. A dictionary, list of tuples, bytes or a file object to send to the specified url
*json		Optional. A JSON object to send to the specified url
*files		Optional. A dictionary of files to send to the specified url
*allow_redirects		Optional. A Boolean to enable/disable redirection.
*Default True (allowing redirects)
*auth		Optional. A tuple to enable a certain HTTP authentication.
*Default None
*cert		Optional. A String or Tuple specifying a cert file or key.
*Default None
*cookies		Optional. A dictionary of cookies to send to the specified url.
*Default None
*headers		Optional. A dictionary of HTTP headers to send to the specified url.
*Default None
*proxies		Optional. A dictionary of the protocol to the proxy url.
*Default None
*stream		Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
*Default False
*timeout		Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
*Default None which means the request will continue until the connection is closed
*verify	
*Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
*Default True



*Operators*
OPERATORS	DESCRIPTION
contains	The field contains a value.
ncontains	The field does not contain a value.
exists	The field exists.
nexists	The field does not exist.
equals	The field equals a value.
nequals	The field does not equal a value.
matches	The field matches a regular expression with RE2 syntax.
nmatches	The field does not match a regular expression with RE2 syntax.



*FIRST ELEMENT	SECOND ELEMENT*
route	The service ID of the target service. You can find the service you want to route to by calling the services endpoint.
suppress	A boolean value indicating whether or not the event should be suppressed.
severity	One of info, warning, error, critical, or unknown.
annotate	The note to set on any new incident created as a result of the event rule.

nexists	The field does not exist.
equals	The field equals a value.
nequals	The field does not equal a value.
matches	The field matches a regular expression with RE2 syntax.
nmatches	The field does not match a regular expression with RE2 syntax.



*FIRST ELEMENT	SECOND ELEMENT*
route	The service ID of the target service. You can find the service you want to route to by calling the services endpoint.
suppress	A boolean value indicating whether or not the event should be suppressed.
severity	One of info, warning, error, critical, or unknown.
annotate	The note to set on any new incident created as a result of the event rule.


