from flask import Flask, render_template

app = Flask(__name__)


characters_data = {
    "kai": {
        "name": "Kai Flameson",
        "image": "kai.png",
        "age": "16",
        "aura": "Fire Aura",
        "kingdom": "Unknown / Fire Kingdom Connection",
        "role": "Main Protagonist",
        "personality": "Silent, calm, serious, determined",
        "description": "Kai Flameson is a silent Fire Aura user who wants to become strong enough to change the unfair world system. In the beginning, Kai does not know the truth about his bloodline, but his Fire Aura carries a hidden mystery connected to the destroyed Fire Kingdom."
    },
    "jinga": {
        "name": "Jinga Flameson",
        "image": "jinga.png",
        "age": "15",
        "aura": "Ice Aura",
        "kingdom": "Unknown / Ice Aura Connection",
        "role": "Kai's Younger Brother",
        "personality": "Funny, emotional, hungry, loyal",
        "description": "Jinga is Kai's cheerful younger brother. He brings comedy and emotion to the story, but deep inside him lies hidden Ice Aura potential that may become important in the future."
    },
    "tyson": {
        "name": "Tyson Hattari",
        "image": "tyson.png",
        "age": "16",
        "aura": "Wind Aura",
        "kingdom": "Wind Kingdom",
        "role": "Rival and Ally",
        "personality": "Confident, sharp, playful, observant",
        "description": "Tyson Hattari is a talented Wind Aura warrior from the Wind Kingdom. He becomes suspicious of Kai after noticing his Fire Aura, and this begins their rivalry."
    },
    "eresawa": {
        "name": "Eresawa",
        "image": "eresawa.png",
        "age": "Unknown",
        "aura": "Mystery Aura / Aura Suppression",
        "kingdom": "Unknown",
        "role": "Academy Teacher",
        "personality": "Calm, dangerous, powerful",
        "description": "Eresawa is a legendary teacher at the Warrior Academy of Sea. He has the ability to suppress Aura and carries deep knowledge about the world's hidden history."
    },
    "free_dela": {
        "name": "Free Dela",
        "image": "free_dela.png",
        "age": "16",
        "aura": "Unknown Aura",
        "kingdom": "Unknown",
        "role": "Elite Student",
        "personality": "Hardworking, silent, strong",
        "description": "Free Dela is one of the strongest academy students. His power comes from hard work, discipline, and an intimidating warrior presence."
    },
    "lui": {
        "name": "Lui",
        "image": "lui.png",
        "age": "16",
        "aura": "Blue Flame Aura",
        "kingdom": "Unknown",
        "role": "Dangerous Student",
        "personality": "Mysterious, dangerous, unpredictable",
        "description": "Lui is a dangerous student with Blue Flame Aura. His energy feels unstable and frightening, making him one of the most mysterious characters in the academy."
    }
}


chapters_data = {
    "episode-1": {
        "title": "Episode 1: New Beginning - Flames of Fate",
        "status": "Story Draft Ready",
        "summary": "Kai and Jinga travel through the forest and meet Tyson. A Sea Gate opens near a lake, forcing the three boys into their first dangerous encounter before they reach the Warrior Academy of Sea.",
        "content": [
            "Opening Narration: In a world ruled by Seven Kingdoms, Aura decides survival. Royals control power while common people struggle.",
            "Scene 1: Kai and Jinga walk through a forest. Jinga complains about hunger while Kai remains silent and focused on his goal.",
            "Scene 2: Tyson appears in the forest and notices Kai's strange Fire Aura. He becomes suspicious because the Fire Kingdom was believed to be destroyed.",
            "Scene 3: At a lake, Jinga drinks water and a Sea Gate suddenly opens. Monsters rise from the water and attack.",
            "Scene 4: Kai tries to use his Fire Aura, but his power is weak and unstable.",
            "Scene 5: Tyson saves Jinga using Wind Aura and defeats the monsters.",
            "Scene 6: After the fight, Kai realizes he must become stronger. The three boys continue toward the Warrior Academy of Sea."
        ]
    },
    "episode-2": {
    "title": "Episode 2: The Others Aura",
    "status": "Released",
    "summary": "Kai, Jinga, and Tyson witness the Aura powers of the other academy students as new friendships and rivalries begin."
},
    "episode-3": {
        "title": "Episode 3: Aura Test",
        "status": "Coming Soon",
        "summary": "Students reveal their aura strength during the academy test.",
        "content": [
            "This episode will focus on aura measurement, rivalries, Free Dela, Lui, and Kai's unstable Fire Aura."
        ]
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/characters")
def characters():
    return render_template("characters.html", characters=characters_data)


@app.route("/character/<name>")
def character_detail(name):
    character = characters_data.get(name)
    return render_template("character_detail.html", character=character)


@app.route("/kingdoms")
def kingdoms():
    return render_template("kingdoms.html")


@app.route("/aura")
def aura():
    return render_template("aura.html")


@app.route("/sea-gates")
def sea_gates():
    return render_template("sea_gates.html")


@app.route("/timeline")
def timeline():
    return render_template("timeline.html")


@app.route("/chapters")
def chapters():
    return render_template("chapters.html", chapters=chapters_data)


@app.route("/chapter/<chapter_id>")
def chapter_detail(chapter_id):
    chapter = chapters_data.get(chapter_id)
    return render_template("chapter_detail.html", chapter=chapter)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/manga/episode-1/<int:page>")
def manga_episode(page):
    total_pages = 18
    return render_template(
        "manga_episode.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-2/<int:page>")
def manga_episode2(page):

    total_pages = 21

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode2.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-3/<int:page>")
def manga_episode3(page):
    total_pages = 11

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode3.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-4/<int:page>")
def manga_episode4(page):

    total_pages = 16

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode4.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-5/<int:page>")
def manga_episode5(page):
    total_pages = 20

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode5.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-6/<int:page>")
def manga_episode6(page):
    total_pages = 18

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode6.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-7/<int:page>")
def manga_episode7(page):
    total_pages = 18

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode7.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-8/<int:page>")
def manga_episode8(page):
    total_pages = 20

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode8.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-9/<int:page>")
def manga_episode9(page):
    total_pages = 20

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode9.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-10/<int:page>")
def manga_episode10(page):
    total_pages = 18

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    return render_template(
        "manga_episode10.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-11/<int:page>")
def manga_episode11(page):
    total_pages = 18

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode11", page=1))

    return render_template(
        "manga_episode11.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-12/<int:page>")
def manga_episode12(page):
    total_pages = 15

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode12", page=1))

    return render_template(
        "manga_episode12.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-13/<int:page>")
def manga_episode13(page):
    total_pages = 15

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode13", page=1))

    return render_template(
        "manga_episode13.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-14/<int:page>")
def manga_episode14(page):
    total_pages = 18

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode14", page=1))

    return render_template(
        "manga_episode14.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-15/<int:page>")
def manga_episode15(page):
    total_pages = 17

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode15", page=1))

    return render_template(
        "manga_episode15.html",
        page=page,
        total_pages=total_pages
    )


@app.route("/manga/episode-16/<int:page>")
def manga_episode16(page):
    total_pages = 18

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode16", page=1))

    return render_template(
        "manga_episode16.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-17/<int:page>")
def manga_episode17(page):
    total_pages = 15

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode17", page=1))

    return render_template(
        "manga_episode17.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-18/<int:page>")
def manga_episode18(page):
    total_pages = 15

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode18", page=1))

    return render_template(
        "manga_episode18.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-19/<int:page>")
def manga_episode19(page):
    total_pages = 15

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode19", page=1))

    return render_template(
        "manga_episode19.html",
        page=page,
        total_pages=total_pages
    )

@app.route("/manga/episode-20/<int:page>")
def manga_episode20(page):
    total_pages = 16

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode20", page=1))

    return render_template(
        "manga_episode20.html",
        page=page,
        total_pages=total_pages
    )

if __name__ == "__main__":
    app.run(debug=True, port=8000)
