from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


# =========================================================
# CHARACTER DATA
# =========================================================

characters_data = {
    "kai": {
        "name": "Kai Flameson",
        "image": "kai.png",
        "age": "16",
        "aura": "Fire Aura",
        "kingdom": "Unknown / Fire Kingdom Connection",
        "role": "Main Protagonist",
        "personality": "Silent, calm, serious, determined",
        "description": "Kai Flameson is a silent Fire Aura user who wants to become strong enough to change the unfair world system."
    },

    "jinga": {
        "name": "Jinga Flameson",
        "image": "jinga.png",
        "age": "15",
        "aura": "Ice Aura",
        "kingdom": "Unknown / Ice Aura Connection",
        "role": "Kai's Younger Brother",
        "personality": "Funny, emotional, hungry, loyal",
        "description": "Jinga is Kai's cheerful younger brother."
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


# =========================================================
# CHAPTER DATA
# =========================================================

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


# =========================================================
# MAIN WEBSITE ROUTES
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/characters")
def characters():
    return render_template(
        "characters.html",
        characters=characters_data
    )


@app.route("/character/<name>")
def character_detail(name):
    character = characters_data.get(name)

    if character is None:
        return redirect(url_for("characters"))

    return render_template(
        "character_detail.html",
        character=character
    )


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
    return render_template(
        "chapters.html",
        chapters=chapters_data
    )


@app.route("/chapter/<chapter_id>")
def chapter_detail(chapter_id):
    chapter = chapters_data.get(chapter_id)

    if chapter is None:
        return redirect(url_for("chapters"))

    return render_template(
        "chapter_detail.html",
        chapter=chapter
    )


@app.route("/about")
def about():
    return render_template("about.html")


# =========================================================
# MANGA EPISODE 1
# =========================================================

@app.route("/manga/episode-1/<int:page>")
def manga_episode(page):
    total_pages = 18

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode", page=1))

    return render_template(
        "manga_episode.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 2
# =========================================================

@app.route("/manga/episode-2/<int:page>")
def manga_episode2(page):
    total_pages = 21

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode2", page=1))

    return render_template(
        "manga_episode2.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 3
# =========================================================

@app.route("/manga/episode-3/<int:page>")
def manga_episode3(page):
    total_pages = 11

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode3", page=1))

    return render_template(
        "manga_episode3.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 4
# =========================================================

@app.route("/manga/episode-4/<int:page>")
def manga_episode4(page):
    total_pages = 16

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode4", page=1))

    return render_template(
        "manga_episode4.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 5
# =========================================================

@app.route("/manga/episode-5/<int:page>")
def manga_episode5(page):
    total_pages = 20

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode5", page=1))

    return render_template(
        "manga_episode5.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 6
# =========================================================

@app.route("/manga/episode-6/<int:page>")
def manga_episode6(page):
    total_pages = 18

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode6", page=1))

    return render_template(
        "manga_episode6.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 7
# =========================================================

@app.route("/manga/episode-7/<int:page>")
def manga_episode7(page):
    total_pages = 18

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode7", page=1))

    return render_template(
        "manga_episode7.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 8
# =========================================================

@app.route("/manga/episode-8/<int:page>")
def manga_episode8(page):
    total_pages = 20

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode8", page=1))

    return render_template(
        "manga_episode8.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 9
# =========================================================

@app.route("/manga/episode-9/<int:page>")
def manga_episode9(page):
    total_pages = 20

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode9", page=1))

    return render_template(
        "manga_episode9.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 10
# =========================================================

@app.route("/manga/episode-10/<int:page>")
def manga_episode10(page):
    total_pages = 18

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode10", page=1))

    return render_template(
        "manga_episode10.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 11
# =========================================================

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


# =========================================================
# MANGA EPISODE 12
# =========================================================

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


# =========================================================
# MANGA EPISODE 13
# =========================================================

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


# =========================================================
# MANGA EPISODE 14
# =========================================================

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


# =========================================================
# MANGA EPISODE 15
# =========================================================

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


# =========================================================
# MANGA EPISODE 16
# =========================================================

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


# =========================================================
# MANGA EPISODE 17
# =========================================================

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


# =========================================================
# MANGA EPISODE 18
# =========================================================

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


# =========================================================
# MANGA EPISODE 19
# =========================================================

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


# =========================================================
# MANGA EPISODE 20
# =========================================================

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


# =========================================================
# MANGA EPISODE 21
# =========================================================

@app.route("/manga/episode-21/<int:page>")
def manga_episode21(page):
    total_pages = 16

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode21", page=1))

    return render_template(
        "manga_episode21.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 22
# =========================================================

@app.route("/manga/episode-22/<int:page>")
def manga_episode22(page):
    total_pages = 15

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode22", page=1))

    return render_template(
        "manga_episode22.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 23
# =========================================================

@app.route("/manga/episode-23/<int:page>")
def manga_episode23(page):
    total_pages = 21

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode23", page=1))

    return render_template(
        "manga_episode23.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 24
# =========================================================

@app.route("/manga/episode-24/<int:page>")
def manga_episode24(page):
    total_pages = 16

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode24", page=1))

    return render_template(
        "manga_episode24.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 25
# =========================================================

@app.route("/manga/episode-25/<int:page>")
def manga_episode25(page):
    total_pages = 20

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode25", page=1))

    return render_template(
        "manga_episode25.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 26
# SEASON 2 - EPISODE 1
# THE BEGINNING OF THE WAR
# =========================================================

@app.route("/manga/episode-26/<int:page>")
def manga_episode26(page):
    total_pages = 15

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode26", page=1))

    return render_template(
        "manga_episode26.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 27
# SEASON 2 - EPISODE 2
# ACADEMY REUNION
# =========================================================

@app.route("/manga/episode-27/<int:page>")
def manga_episode27(page):
    total_pages = 24

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode27", page=1))

    return render_template(
        "manga_episode27.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 28
# SEASON 2 - EPISODE 3
# The First Mission
# =========================================================

@app.route("/manga/episode-28/<int:page>")
def manga_episode28(page):
    total_pages = 18

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode28", page=1))

    return render_template(
        "manga_episode28.html",
        page=page,
        total_pages=total_pages
    )


# =========================================================
# MANGA EPISODE 29
# SEASON 2 - EPISODE 4
# Dragon Island
# =========================================================

@app.route("/manga/episode-29/<int:page>")
def manga_episode29(page):
    total_pages = 16

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode29", page=1))

    return render_template(
        "manga_episode29.html",
        page=page,
        total_pages=total_pages
    )




# =========================================================
# MANGA EPISODE 30
# SEASON 2 - EPISODE 5
# The New Warrior
# =========================================================

@app.route("/manga/episode-30/<int:page>")
def manga_episode30(page):
    total_pages = 16

    if page < 1 or page > total_pages:
        return redirect(url_for("manga_episode30", page=1))

    return render_template(
        "manga_episode30.html",
        page=page,
        total_pages=total_pages
    )




# =========================================================
# START FLASK SERVER
# =========================================================

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000
    )
