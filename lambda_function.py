import json
import urllib.request
from base64 import b64encode

def lambda_handler(event, context):
    # Print the event to debug and see the content
    print("Received event:", json.dumps(event, indent=2))
    
    # Check if the event is an EC2 instance state change (i.e., instance launch)
    if event['detail']['state'] == 'running':
        # Get EC2 instance ID and other details from the event
        instance_id = event['detail']['instance-id']
        print(f"EC2 Instance {instance_id} is running.")
        
        # Jenkins URL and API Token
        jenkins_url = 'http://http://13.61.88.114:8080'
        job_name = 'job'
        username = 'admin'
        api_token = 'jenkins-api-token'
        
        # Jenkins job trigger URL
        url = f"{jenkins_url}/job/{job_name}/build"
        
        # Encode username and API token for Basic Authentication
        credentials = b64encode(f'{username}:{api_token}'.encode('utf-8')).decode('utf-8')
        
        # Set headers for authentication
        headers = {
            'Authorization': f'Basic {credentials}'
        }
        
        # Create a request to trigger the Jenkins job
        req = urllib.request.Request(url, headers=headers, method='POST')
        
        try:
            response = urllib.request.urlopen(req)
            status_code = response.getcode()
            if status_code == 201:
                return {
                    'statusCode': 200,
                    'body': json.dumps(f"Jenkins Pipeline triggered successfully for instance {instance_id}")
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps(f'Error triggering Jenkins pipeline: {status_code}')
                }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error: {str(e)}')
            }

    else:
        # If the instance is not in the 'running' state, handle other states (e.g., stopped, terminated)
        print(f"EC2 instance {event['detail']['instance-id']} is not in the 'running' state. No action taken.")
        return {
            'statusCode': 200,
            'body': json.dumps(f"No action for state: {event['detail']['state']}")
        }
