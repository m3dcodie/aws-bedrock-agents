import boto3
import json

client = boto3.client('bedrock-agentcore', region_name='ap-southeast-2')
payload = json.dumps({
    "input": {"prompt": "What is 2+2?"}
})

response = client.invoke_agent_runtime(
    agentRuntimeArn='arn:aws:bedrock-agentcore:ap-southeast-2:235494807105:runtime/strands_nova_getting_started-DosldVC56T',
    runtimeSessionId='dfmeoagmreaklgmrkleafremoigrmtesogmtrskhmtkrlshmt',  # Must be 33+ chars
    payload=payload,
    qualifier="DEFAULT" # Optional
)
response_body = response['response'].read()
response_data = json.loads(response_body)
print("Agent Response:", response_data)