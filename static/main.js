const randomBackgroundLight = () => {
    var images = ["Beach\ Pier.jpg", "Cliff\ Fog.jpg", "Foggy\ Sunrise.jpg", "Forest\ Landscape.jpg" , 
    "Mountain\ Sky.jpg", "Pink\ Mountain.jpg", "Rocky\ Sea.jpg", "Water\ Sun.jpg",];
    document.getElementsByTagName("main")[0].style.backgroundImage = 
    "url('backgrounds/" + images[Math.floor(Math.random() * images.length)] + "')";
    var img = document.getElementsByTagName("main")[0].style.backgroundImage;
    if(img == 'url("backgrounds/Pink\ Mountain.jpg")' || img == 'url("backgrounds/Mountain\ Sky.jpg")'){
        document.getElementsByTagName("main")[0].style.backgroundPosition = "center bottom";
    }
    else{
        document.getElementsByTagName("main")[0].style.backgroundPosition = "center center";
    }
}

const randomBackgroundDark = () => {
    var images = ["Canopy\ Road.jpg", "Fall\ Road.jpg", "Foggy\ Mountain.jpg", "Foggy\ Trees.jpg", 
    "Green\ Leaves.jpg", "Mountain\ Lake.jpg", "Night\ Scene.jpg", "Rocky\ Waterfall.jpg", "Star\ Sky.jpg",];
    document.getElementsByTagName("main")[0].style.backgroundImage = 
    "url('backgrounds/Dark/" + images[Math.floor(Math.random() * images.length)] + "')";
    var img = document.getElementsByTagName("main")[0].style.backgroundImage;
    if(img == 'url("backgrounds/Dark/Foggy\ Mountain.jpg")' || img == 'url("backgrounds/Dark/Foggy\ Trees.jpg")'){
        document.getElementsByTagName("main")[0].style.backgroundPosition = "center bottom";
    }
    else{
        document.getElementsByTagName("main")[0].style.backgroundPosition = "center center";
    }
}

const navSlide = () => {
    const hamburger = document.querySelector('.hamburger');
    const social = document.querySelector('.social-links');
    let menuOpen = false;
    hamburger.addEventListener('click', () => {
        if(!menuOpen) {
            hamburger.classList.add('open');
            menuOpen = true;
            social.classList.add('active');
        }
        else {
            hamburger.classList.remove('open');
            social.classList.remove('active');
            menuOpen = false;
        }
    })
}

const darkMode = () => {
    const toggle = document.getElementById('light-dark-toggle');
    const hamburger = document.querySelector('.hamburger');
    const header = document.getElementsByTagName("header")[0];
    const site_name = document.querySelector(".site-name");
    const backbox = document.querySelector(".backbox");
    const instasnakes = document.querySelector(".insta-snakes");
    const preface = document.querySelector(".preface");
    const radios = document.querySelector(".radios");
    const label = document.querySelectorAll(".label");
    const button = document.getElementsByTagName("button")[0];
    const loadw = document.querySelector(".load-warn");
    const darkp = document.querySelector(".darkprompt");
    const req = document.querySelector(".request");
    const idiot = document.querySelector(".idiot");
    const finuname = document.querySelector(".final-username");
    const uname = document.querySelectorAll(".username-display");
    const name = document.querySelectorAll(".name-display");
    const unfollowers = document.querySelector(".unfollowers");
    toggle.addEventListener('click', () => {
        if(!toggle.checked) {
            randomBackgroundLight();
            hamburger.classList.remove('dark');
            header.classList.remove('dark');
            site_name.classList.remove('dark');
            backbox.classList.remove('dark');
            instasnakes.classList.remove('dark');
            try{
                preface.classList.remove('dark');
                radios.classList.remove('dark');
                label[0].classList.remove('dark');
                label[1].classList.remove('dark');
                button.classList.remove('dark');
            }
            catch{}
            try{
                loadw.classList.remove('dark');
                darkp.classList.remove('dark');
            }
            catch{}
            try{
                req.classList.remove('dark');
            }
            catch{}
            try{
                idiot.classList.remove('dark');
            }
            catch{}
            try{
                finuname.classList.remove('dark');
                uname.forEach(item => item.querySelector('a').classList.remove('dark'));
                name.forEach(item => item.classList.remove('dark'));
                unfollowers.classList.remove('dark');
            }
            catch{}
        }
        else {
            randomBackgroundDark();
            hamburger.classList.add('dark');
            header.classList.add('dark');
            site_name.classList.add('dark');
            backbox.classList.add('dark');
            instasnakes.classList.add('dark');
            try{
                preface.classList.add('dark');
                radios.classList.add('dark');
                label[0].classList.add('dark');
                label[1].classList.add('dark');
                button.classList.add('dark');
            }
            catch{}
            try{
                loadw.classList.add('dark');
                darkp.classList.add('dark');
            }
            catch{}
            try{
                req.classList.add('dark');
            }
            catch{}
            try{
                idiot.classList.add('dark');
            }
            catch{}
            try{
                finuname.classList.add('dark');
                uname.forEach(item => item.querySelector('a').classList.add('dark'));
                name.forEach(item => item.classList.add('dark'));
                unfollowers.classList.add('dark');
            }
            catch{}
        }
    })
}

const animateUsername = () => {
    try{
        jQuery.support.placeholder = () => {
            var i = document.createElement('input');
            return 'placeholder' in i;
        }
        var label = document.getElementById("username-label"),
            input = document.getElementById("username-input");
        if (jQuery.support.placeholder) {
            label.classList.add('hide-label');
            var str = input.value;
            input.onkeyup = () => {
                str = input.value;
                if (str == ''){
                    label.classList.remove('unhighlight-label');
                    label.classList.add('hide-label');
                }
                else {
                    label.classList.remove('hide-label');
                }
            };
            input.onblur = () => {
                str = input.value;
                if( str == '' ){
                    label.classList.add('hide-label');
                } 
                else {
                    label.classList.remove('hide-label');
                    label.classList.add('unhighlight-label');
                }
            };
            input.onfocus = () => {
                str = input.value;
                if( str !== '' ){
                    label.classList.remove('unhighlight-label');
                } 
            };
        }
    }
    catch{};
}

const app = () => {
    window.onload = randomBackgroundLight();
    navSlide();
    darkMode();
    animateUsername();
}

app();
