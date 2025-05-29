from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcripcion', methods=['GET'])
def transcripcion():
    video_id = request.args.get('videoId')
    if not video_id:
        return jsonify({"error": "Falta el parámetro videoId"}), 400
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["es", "en"])
        texto = " ".join([x['text'] for x in transcript])
        return jsonify({
            "videoId": video_id,
            "transcripcion": texto
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
