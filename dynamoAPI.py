from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

region_name="eu-west-3"
aws_access_key_id="ASIAZGTIYK2P5XEXIJ4P"
aws_secret_access_key="l3eknXqemR3t+gAJqjDyaVt7IwEKkim+CjKFafK9"
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjECwaCmFwLXNvdXRoLTEiRjBEAiAiMIZHQe3ZYsoYBpL1IBCJLu5Ah5IxDlNNQe9rDA6vjAIgb0T32kb75K2fzIMNcuMpgPVBJLEwKf61/OmPWEFf7SQqtAII1f//////////ARABGgw2MzI2NTM2MzMxODMiDOHAh8V24xQQqSEJIyqIAiflsSWK84W4uo1k+knPAK6VJAlXu1DhzoRHQWmCMK9CEnM6AfdX6AP5ST95WpB3jKdD9/bO6FoPnoUlieKNE4zO0lFUbVQhxxrsXwonNkUtEuhYYrxifDtqVerhOJehKd9OK0Yz5XfekGetCXBhdnk3FcftlWDHb4grZif4sVXm+Ot1i48rJMUKDmgrhYBooPbmE6uwK5PedO13OI438g1X3uzHHer59ah/fbjkbKmhwKDIBGXHzyFCD7Clqtqh0wNUu74lyRIfJfpT/S6EW2otbcxzCspIBBulYa+qtPXqaSLZpX6ZmD8PoLc3sH66BXvBgfLv6kN9Z4uB5mxi3gwqRzSk9SdUWDCSoqStBjqeAbGES2rDkRDjpYnGVdufBAg8xK/XlFASVBDOpidewzHBKFa4kyMXP+2GjOQj5lK/0+lqZJxtDNbP1qBGGk88Fhhdo/R2atoBNTwPNu0TxsWR74CUfoifiK8wkwSwJkxpKEzIun4v4krPvhw6AN3Za86hqRe7kbyZqCnxqSjfYIs+1G/rQkVaMQmFPsh0Zb84FGAtIBZVbcO30dvFrvT0"
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
    aws_session_token=AWS_SESSION_TOKEN,
)

#dynamodb = boto3.resource('dynamodb',region_name = 'ap-northeast-1')  # Replace 'your-region' with your AWS region
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
