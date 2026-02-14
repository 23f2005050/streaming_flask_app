
from flask import Flask, Response, request, stream_with_context
from flask_cors import CORS
import json
import time

app = Flask(__name__)
CORS(app)

def generate_stream(prompt):
    try:
        chunks = [
    "📊 Insight 1: AI adoption is accelerating across industries. Organizations across healthcare, finance, retail, and manufacturing are rapidly integrating AI-driven solutions to improve efficiency, reduce errors, and enhance decision-making processes. This widespread adoption signals a long-term structural shift rather than a temporary trend. ",
    "📈 Insight 2: Early adopters gain measurable advantages. Companies investing early in AI technologies often achieve superior productivity, stronger customer engagement, and better operational scalability. These advantages compound over time, making it increasingly difficult for late adopters to catch up with competitors already benefiting from optimized systems. ",
    "💰 Insight 3: Automation reduces operational costs over time. AI-powered automation significantly lowers expenses associated with repetitive tasks, manual data processing, and human error correction. Although initial implementation costs may be high, long-term savings typically outweigh upfront investments, improving overall profitability. ",
    "🌍 Insight 4: Emerging markets show strong digital growth. Developing economies are experiencing rapid digital transformation, driven by mobile-first technologies, cloud computing, and AI-enabled services. This growth presents substantial opportunities for businesses seeking new customer bases and expansion strategies. ",
    "🔮 Insight 5: Personalization drives engagement metrics. AI enables hyper-personalized user experiences by analyzing behavioral data, preferences, and interaction patterns. Personalized content and recommendations improve customer satisfaction, retention rates, and conversion metrics across digital platforms. ",
    "⚡ Insight 6: Faster inference improves user experience. Advances in model optimization and hardware acceleration allow AI systems to deliver responses with minimal latency. Reduced response times enhance usability, particularly in interactive applications such as chatbots, virtual assistants, and real-time analytics tools. ",
    "🧩 Insight 7: Integration complexity remains a barrier. Despite AI benefits, many organizations struggle with system integration, data compatibility, and infrastructure upgrades. Addressing these challenges requires strategic planning, skilled expertise, and ongoing technical investment. ",
    "🏁 Insight 8: Ethical AI regulations are expanding globally. Governments and regulatory bodies are introducing frameworks to ensure responsible AI usage, focusing on transparency, fairness, data privacy, and accountability. Compliance with evolving regulations is becoming a critical component of AI strategy."
]

        for chunk in chunks:
            data = json.dumps({"content": chunk})
            yield f"data: {data}\n\n"
            time.sleep(0.2)

        yield "data: [DONE]\n\n"

    except Exception as e:
        error = json.dumps({"error": str(e)})
        yield f"data: {error}\n\n"

@app.route("/stream", methods=["POST"])
def stream():
    data = request.json
    prompt = data.get("prompt", "")

    return Response(
        stream_with_context(generate_stream(prompt)),
        content_type="text/event-stream"
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
