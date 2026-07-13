import json

class AuctionBidHistoryValidator:
    def validate(self, data):
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        
        required_fields = ['user_id', 'auction_id', 'bid_amount', 'timestamp']
        for field in required_fields:
            if field not in data:
                raise KeyError(f"Missing required field: {field}")
        
        self.validate_user_id(data['user_id'])
        self.validate_auction_id(data['auction_id'])
        self.validate_bid_amount(data['bid_amount'])
        self.validate_timestamp(data['timestamp'])

    def validate_user_id(self, user_id):
        if not isinstance(user_id, str) or len(user_id.strip()) == 0:
            raise ValueError("User ID must be a non-empty string")

    def validate_auction_id(self, auction_id):
        if not isinstance(auction_id, str) or len(auction_id.strip()) == 0:
            raise ValueError("Auction ID must be a non-empty string")

    def validate_bid_amount(self, bid_amount):
        if not isinstance(bid_amount, (int, float)) or bid_amount <= 0:
            raise ValueError("Bid amount must be a positive number")

    def validate_timestamp(self, timestamp):
        if not isinstance(timestamp, str) or len(timestamp.strip()) == 0:
            raise ValueError("Timestamp must be a non-empty string")
        try:
            json.loads(f'"{timestamp}"')  # Simple check to ensure it's a valid ISO format
        except json.JSONDecodeError:
            raise ValueError("Invalid timestamp format")

class BidHistoryMapper:
    def map_to_internal_format(self, data):
        validator = AuctionBidHistoryValidator()
        validator.validate(data)
        
        return {
            'user_id': data['user_id'],
            'auction_id': data['auction_id'],
            'bid_amount': data['bid_amount'],
            'timestamp': data['timestamp']
        }

# Example usage:
data = {
    "user_id": "user123",
    "auction_id": "auction456",
    "bid_amount": 100.5,
    "timestamp": "2023-04-30T12:34:56Z"
}

mapper = BidHistoryMapper()
internal_data = mapper.map_to_internal_format(data)
print(internal_data)
```

This Python code defines a utility for validating and mapping data related to Yahoo!オークション落札履歴取得・領収書保存ツール. The `AuctionBidHistoryValidator` class ensures that the input data contains all required fields and that each field is of the correct type and format. The `BidHistoryMapper` class uses this validator to validate the data before mapping it into an internal format suitable for further processing or storage.