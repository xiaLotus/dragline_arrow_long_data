import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def load_json():
    """讀取 nodes.json 檔案"""
    try:
        with open("nodes.json", "r", encoding="utf-8") as f:
            nodes = json.load(f)
        print(f"✅ 成功載入 {len(nodes)} 個節點")
        return nodes
    except FileNotFoundError:
        print("❌ nodes.json 檔案不存在")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式錯誤：{e}")
        return []
    except Exception as e:
        print(f"❌ 讀取檔案時發生錯誤：{e}")
        return []

@app.route('/nodes', methods=['GET'])
def get_nodes():
    """API 端點：獲取節點資料"""
    try:
        nodes = load_json()
        return jsonify(nodes)
    except Exception as e:
        print(f"❌ API 錯誤：{e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 啟動 Flask 應用...")
    app.run(debug=True, host='0.0.0.0', port=5000)