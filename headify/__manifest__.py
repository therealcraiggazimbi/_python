# -*- coding: utf-8 -*-
{
    "name": "Headify",
    "summary": """
    Revamp the website header with an engaging image cover and intuitive hamburger menu for seamless navigation on your Odoo website.""",
    "description": """
        Headify aims to elevate the visual appeal and functionality of your Odoo website header. By implementing a comprehensive revamp, we focus on enhancing user experience through engaging image covers and an intuitive hamburger menu. With these enhancements, navigating your Odoo website becomes seamless and effortless for visitors. The new header design not only captivates attention with striking visuals but also ensures easy access to essential navigation options, facilitating smoother interaction and exploration of your website's content. By incorporating these features, our module aims to elevate the overall user experience, driving higher engagement and satisfaction levels among your website visitors.
    """,
    "author": "Craig Gazimbi",
    "website": "https://github.com/therealcraiggazimbi/_python/tree/main/headify",
    "category": "Website",
    "version": "0.0.1",
    "depends": ["base", "headify"],
    "data": ["views/header.xml", "views/css_loader.xml"],
    "demo": [
        "views/header.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
