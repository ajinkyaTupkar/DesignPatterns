'''
Adapter Pattern Example: Adapting REST API to SOAP Interface

Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces, enabling them to communicate.
This pattern is particularly useful when integrating third-party libraries or services that do not conform to the expected interface of your application.

Cons
- Can introduce additional complexity by adding an extra layer of abstraction.
- May lead to performance overhead due to the additional processing required for adaptation.
- Can make the code harder to understand if not implemented carefully, as it may obscure the original interfaces.
- Can lead to tight coupling between the adapter and the adapted interfaces, making it harder to change either interface independently.
Pros
- Promotes code reusability by allowing existing code to work with new interfaces without modification.
- Enables integration of third-party libraries or services that do not conform to the expected interface.
- Follows the Open/Closed Principle, allowing for easy extension of the codebase by adding new adapters without modifying existing code.
- Simplifies the client code by providing a consistent interface to interact with different implementations.
Uses
- When integrating third-party libraries or services that do not conform to the expected interface of your application.
- When you need to adapt an existing interface to a new one without modifying the original code.
- When you want to create a reusable component that can work with multiple interfaces.
'''


class RESTAPIClient:
    def get_data(self):
        # Simulate getting data from a REST API
        return {"status": "success", "data": {"value": 42}}

class SOAPServerInterface:
    def fetch_data(self):
        pass

class SOAPServer(SOAPServerInterface):
    def fetch_data(self):
        # Simulate fetching data via SOAP
        return "<response><status>success</status><value>42</value></response>"

class RESTToSOAPAdapter(SOAPServerInterface):
    def __init__(self, rest_client):
        self.rest_client = rest_client

    def fetch_data(self):
        # Adapts REST API response to SOAP-like response
        rest_response = self.rest_client.get_data()
        status = rest_response["status"]
        value = rest_response["data"]["value"]
        return f"<response><status>{status}</status><value>{value}</value></response>"

# Client code expecting SOAPServerInterface
def process_data(soap_server):
    print("Processing data from SOAP server:")
    print(soap_server.fetch_data())

if __name__ == "__main__":
    rest_client = RESTAPIClient()
    adapter = RESTToSOAPAdapter(rest_client)
    process_data(adapter)