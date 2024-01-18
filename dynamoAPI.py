from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Replace these values with your AWS credentials and DynamoDB table details
# aws_access_key_id = 'ASIA4LDMLOPFNKWNGREI'
# aws_secret_access_key = 'RCvspb2rqegsZUhx7XKx3YCscpmvwsxFH5JnErm8'
# region_name = 'ap-northeast-1'
# table_name = 'super-panama-hat-fawnCyclicDB'
# 
# AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjECsaCmFwLXNvdXRoLTEiRzBFAiEAuiMYlOiWKqfnS0dQMTzJ4tt1yNszpXWobVOHw2MCdGgCIFb2h/qKt4qw5JQUoMsCBNwGo9QDm6u5cjcfm5Y4uWa0KrgCCNT//////////wEQABoMODQ4NDgzMjgzOTE0Igzro+LbzMsBcvUyfTgqjAKJDMe3Wo5oEwcRiBmbCAN9WLfzbxXghbWeCv3Wk4VPEHWERPndLxqQ4EAGPmstQdYg4V7dWfcP3420xxALMxI35fLl3RHEK1WFlk0YZJr2SLzlLZ8BYYvhG2B3tx9f+SONzqgRhfgiwYnhcNtAe/qeG5RUuZpl8YWUI2K9NIHEmTyo+t0sTpplbhvlCjviLb+RAbs4mIJ+Z3vcJE0e8Q1cIEnO7L16xrlaQVK8FGqs/1vqCMW1DXfNQanbA35aq5eAeTpe/4WhnIgAJSf+VTpnc+aoGY3R6JBSGWUonJ7b8vBiEZn3g5jCwOxVhmzjT0XHCmryPTsHRG2l1DN/0jBSQli98cGlcFO9gczlMMmMpK0GOp0BTqD3z42AKHKIdRfqJTw7gga0c8l4kWlDnmYcQQOnk7a69pPWBdWqhYudEHG1beVUyzAJYaPTxc3DJUTjozebLirD0PZ7nrs1zrdaBRyAn3R27FCuE2GjE64WeJ+REoVD4SzJfUl8+XgP13uDv3WoMkPBN3uO4LJ9+f7p2eati/p+Z2d43WOOpyMPvxObCvBOoXM4GIwP2uUJkfJm4w=="
# # Create a DynamoDB resource
# dynamodb = boto3.resource(
#     'dynamodb',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key,
#     region_name=region_name,
#     aws_session_token=AWS_SESSION_TOKEN,
# )
# Initialize DynamoDB client
aws_access_key_id = 'ASIA4LDMLOPFNKWNGREI'
aws_secret_access_key = 'RCvspb2rqegsZUhx7XKx3YCscpmvwsxFH5JnErm8'
region_name = 'ap-northeast-1'
table_name = 'super-panama-hat-fawnCyclicDB'

AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjECsaCmFwLXNvdXRoLTEiRzBFAiEAuiMYlOiWKqfnS0dQMTzJ4tt1yNszpXWobVOHw2MCdGgCIFb2h/qKt4qw5JQUoMsCBNwGo9QDm6u5cjcfm5Y4uWa0KrgCCNT//////////wEQABoMODQ4NDgzMjgzOTE0Igzro+LbzMsBcvUyfTgqjAKJDMe3Wo5oEwcRiBmbCAN9WLfzbxXghbWeCv3Wk4VPEHWERPndLxqQ4EAGPmstQdYg4V7dWfcP3420xxALMxI35fLl3RHEK1WFlk0YZJr2SLzlLZ8BYYvhG2B3tx9f+SONzqgRhfgiwYnhcNtAe/qeG5RUuZpl8YWUI2K9NIHEmTyo+t0sTpplbhvlCjviLb+RAbs4mIJ+Z3vcJE0e8Q1cIEnO7L16xrlaQVK8FGqs/1vqCMW1DXfNQanbA35aq5eAeTpe/4WhnIgAJSf+VTpnc+aoGY3R6JBSGWUonJ7b8vBiEZn3g5jCwOxVhmzjT0XHCmryPTsHRG2l1DN/0jBSQli98cGlcFO9gczlMMmMpK0GOp0BTqD3z42AKHKIdRfqJTw7gga0c8l4kWlDnmYcQQOnk7a69pPWBdWqhYudEHG1beVUyzAJYaPTxc3DJUTjozebLirD0PZ7nrs1zrdaBRyAn3R27FCuE2GjE64WeJ+REoVD4SzJfUl8+XgP13uDv3WoMkPBN3uO4LJ9+f7p2eati/p+Z2d43WOOpyMPvxObCvBOoXM4GIwP2uUJkfJm4w=="
# Create a DynamoDB resource

dynamodb = boto3.resource('dynamodb',region_name = 'ap-northeast-1')  # Replace 'your-region' with your AWS region
table_name = 'super-panama-hat-fawnCyclicDB'  # Replace with your DynamoDB table name
table = dynamodb.Table(table_name)


@app.route('/store_health_data', methods=['POST'])
def store_health_data():
    # Get data from the request
    data = request.json

    # Create a new HealthInsurance item
    health_data = {
        'pk': data['mobile'],
        'sk': 'user',
        'name': data['name'],
        'age': data['age'],
        'mobile': data['mobile'],
        'email': data['email'],
        'gender': data['gender'],
        'plan': data['plan'],
        'pan': data['pan'],
        'dob': data['dob'],
        'nominee_name': data['nominee_name'],
        'nominee_details': data['nominee_details'],
        'nominee_gender': data['nominee_gender'],
        'proposer_name': data['proposer_name'],
        'proposer_gender': data['proposer_gender']
    }

    # Put the item into DynamoDB
    table.put_item(Item=health_data)

    return jsonify({"message": "Health data stored successfully"}), 201


@app.route('/get_health_data', methods=['GET'])
def get_health_data():
    response = table.scan()
    health_data = response.get('Items', [])

    data_list = []
    print(health_data)
    for data in health_data:
        data_list.append({
            'name': data['name'],
            'age': data['age'],
            'mobile': data['mobile'],
            'email': data['email'],
            'gender': data['gender'],
            'plan': data['plan'],
            'pan': data['pan'],
            'dob': data['dob'],
            'nominee_name': data['nominee_name'],
            'nominee_gender': data['nominee_gender'],
            'proposer_name': data['proposer_name'],
            'nominee_details': data['nominee_details'],
            'proposer_gender': data['proposer_gender']
        })

    return jsonify({"health_data": data_list})


@app.route('/get_health_data_by_mobile/<mobile>', methods=['GET'])
def get_health_data_by_mobile(mobile):
    response = table.get_item(Key={'pk': mobile, 'sk': 'user'})
    health_data = response.get('Item', None)

    if health_data:
        return jsonify({
            'name': health_data['name'],
            'age': health_data['age'],
            'mobile': health_data['mobile'],
            'email': health_data['email'],
            'gender': health_data['gender'],
            'plan': health_data['plan'],
            'pan': health_data['pan'],
            'dob': health_data['dob'],
            'nominee_name': health_data['nominee_name'],
            'nominee_gender': health_data['nominee_gender'],
            'proposer_name': health_data['proposer_name'],
            'nominee_details': health_data['nominee_details'],
            'proposer_gender': health_data['proposer_gender']
        })
    else:
        return jsonify({"message": "Health data not found for the given mobile number"}), 404


@app.route('/delete_health_data_by_mobile/<mobile>', methods=['DELETE'])
def del_health_data(mobile):
    response = table.delete_item(Key={'pk': mobile, 'sk': 'user'})

    if response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
        return jsonify({"message": "Health data deleted successfully"}), 200
    else:
        return jsonify({"message": "Health data not found for the given mobile number"}), 404


if __name__ == '__main__':
    app.run(debug=True)
