from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
def get_db_connection():
    conn = sqlite3.connect('auctions.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/auctions', methods=['POST'])
def create_auction():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO auctions (item_id, buyer_name, bid_amount) VALUES (?, ?, ?)',
                   (data['item_id'], data['buyer_name'], data['bid_amount']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Auction created successfully'}), 201

@app.route('/api/auctions', methods=['GET'])
def get_auctions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM auctions')
    auctions = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in auctions])

@app.route('/api/receipts', methods=['POST'])
def create_receipt():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO receipts (auction_id, buyer_name, total_amount) VALUES (?, ?, ?)',
                   (data['auction_id'], data['buyer_name'], data['total_amount']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Receipt created successfully'}), 201

@app.route('/api/receipts', methods=['GET'])
def get_receipts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM receipts')
    receipts = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in receipts])

if __name__ == '__main__':
    app.run(debug=True)
```

This is a basic Flask application with two sets of API endpoints: one for managing auction records and another for managing receipt records. It uses SQLite as the database, which you'll need to create and populate accordingly. The `create_auction` and `create_receipt` functions handle POST requests to add new records, while `get_auctions` and `get_receipts` handle GET requests to retrieve all records from their respective tables.