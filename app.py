from flask import Flask, render_template
import random

app = Flask(__name__)

car_data = [
    {
        "model": "Toyota Supra Mark 4",
        "fact": "Famous for its 2JZ engine and a favorite in the tuner world.",
        "specs": "3.0L Twin-Turbo I6, 276 hp, 0–60 in 4.6 sec, Top Speed 155 mph",
        "image": "/static/images/supra.jpg",
        "video_url": "https://www.youtube.com/embed/cwKAS9vQq90",
        "wiki_url": "https://en.wikipedia.org/wiki/Toyota_Supra"
    },
    {
        "model": "Nissan GTR R35",
        "fact": "The Nissan GT-R’s dashboard graphics were designed by Polyphony Digital, the same developers behind the Gran Turismo series. ",
        "specs": "3.8L Twin-Turbo V6, 565 hp, 0–60 in 2.9 sec, Top Speed 196 mph",
        "image": "/static/images/gtr.jpg",
        "video_url": "https://www.youtube.com/embed/YXFSVoVqhYw?si=G2jiK04fI7-1Gb49",
        "wiki_url": "https://en.wikipedia.org/wiki/Nissan_GT-R"
    },
    {
        "model": "EK Honda Civic Type R",
        "fact": "Lightweight and high-revving, it was a true VTEC legend.",
        "specs": "1.6L I4 VTEC, 185 hp, 0–60 in ~6.7 sec",
        "image": "/static/images/civic.jpg",
        "video_url": "https://www.youtube.com/embed/cAvZpD-Fp5g?si=nMQ0k4Y2dtrM4hD6",
        "wiki_url": "https://en.wikipedia.org/wiki/Honda_Civic_Type_R"
    },
    {
        "model": "BMW M5 CS",
        "fact": "The BMW M5 CS features M Carbon bucket seats for both the driver and front passenger, along with individual rear bucket seats, resulting in a four-seat configuration.",
        "specs": "4.4L Twin-Turbo V8, 627 hp, 0–60 in 2.9 sec",
        "image": "/static/images/m5.jpg",
        "video_url": "https://www.youtube.com/embed/vQXvyV0zIP4?si=H7s4aGA-MkRes7tN",
        "wiki_url": "https://en.wikipedia.org/wiki/BMW_M5#F90_M5_CS_(2021)"
    },
    {
        "model": "Koenigsegg Jesko",
        "fact": "A Swedish hypercar built for both track and top speed records.",
        "specs": "5.0L Twin-Turbo V8, up to 1600 hp, Top Speed ~310+ mph",
        "image": "/static/images/jesko.jpg",
        "video_url": "https://www.youtube.com/embed/6xY_LQzTyus?si=ukBq6WMp4w-bFQ8x",
        "wiki_url": "https://en.wikipedia.org/wiki/Koenigsegg_Jesko"
    },
    {
        "model": "Lamborghini Sesto Elemento",
        "fact": "One of the lightest Lamborghinis ever made using carbon fiber.",
        "specs": "5.2L V10, 562 hp, 0–60 in 2.5 sec",
        "image": "/static/images/sesto.jpg",
        "video_url": "https://www.youtube.com/embed/zRT1hw_-0a8?si=nbrvyU550aYLBeEa",
        "wiki_url": "https://en.wikipedia.org/wiki/Lamborghini_Sesto_Elemento"
    },
    {
        "model": "1997 Mercedes-Benz CLK GTR",
        "fact": "A Le Mans racer turned into a street-legal hypercar.",
        "specs": "6.9L V12, 604 hp, Top Speed 214 mph",
        "image": "/static/images/clk_gtr.jpg",
        "video_url": "https://www.youtube.com/embed/ZlLy3Va1a30?si=-EnkxMOQG_yymmTB",
        "wiki_url": "https://en.wikipedia.org/wiki/Mercedes-Benz_CLK_GTR"
    },
    {
        "model": "Dodge Challenger SRT Demon 170",
        "fact": "The fastest quarter-mile production car ever built.",
        "specs": "6.2L Supercharged V8, 1025 hp, 0–60 in 1.66 sec",
        "image": "/static/images/demon.jpg",
        "video_url": "https://www.youtube.com/embed/-aHn0Hk7OCg?si=xnGD2rtZHgKmjpBO",
        "wiki_url": "https://en.wikipedia.org/wiki/Dodge_Challenger_SRT_Demon"
    },
    {
        "model": "Nissan Skyline R34",
        "fact": "The Nissan Skyline R34, equipped with the RB26DETT engine, became an icon in the tuning world and was immortalized in the Fast & Furious franchise. It featured advanced technology, including a multi-function dashboard and an AWD system.",
        "specs": "2.6L twin-turbo I6, 280 hp, AWD",
        "image": "/static/images/r34.jpg",
        "video_url": "https://www.youtube.com/embed/9mhOJggoa_Q?si=A2a7VGeQDrP4yoUG",
        "wiki_url": "https://en.wikipedia.org/wiki/Nissan_Skyline_GTR"
    },
    {
        "model": "Lexus LFA",
        "fact": "Known for its high-revving V10 and F1-like sound.",
        "specs": "4.8L V10, 552 hp, 0–60 in 3.6 sec",
        "image": "/static/images/lfa.jpg",
        "video_url": "https://www.youtube.com/embed/wZvvvfWsw9w?si=D8yOWVCn0BRd58IL",
        "wiki_url": "https://en.wikipedia.org/wiki/Lexus_LFA"
    }
]

@app.route("/")
def index():
    car = random.choice(car_data)
    return render_template("index.html", car=car)

if __name__ == "__main__":
    app.run(debug=True)
