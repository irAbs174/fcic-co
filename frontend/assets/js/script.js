/***
 * Loader
 */

var tll = new TimelineMax({onComplete: hide_loader})
var l = document.querySelector('.left');
var r = document.querySelector('.right');
var logo = document.querySelector('.loading-logo');

tll.to(logo, 1, {
    color: '#f9f9f9',
    opacity: 0,
    scale: 1.05,
    ease: Power0.easeOut
})
TweenMax.to(l, 1, {
    delay: 1,
    opacity: 0,
    x: '-100%', //translateX
    ease: Power1.easeOut
})
TweenMax.to(r, 1, {
    delay: 1,
    opacity: 0,
    x: '100%', //translateX
    ease: Power1.easeOut
})

function hide_loader() {
    gsap.to(".loading", {
        duration: 1, opacity: 0, onComplete: function () {
            document.getElementById("loading").remove();
        }
    });

}

/***
 * Sliders
 */
const main_slider = new Swiper('.main-slider', {
    slidesPerView: 3,
    spaceBetween: 30,
    rtl: true,
    centeredSlides: true,
    centeredSlidesBounds: true,
    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    grabCursor: true,
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 40,
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 50,
        },
    }
})
const option_slider = new Swiper('.option-slider', {
    slidesPerView: 3,
    spaceBetween: 30,
    rtl: true,
    centeredSlides: true,
    centeredSlidesBounds: true,
    loop: true,
    grabCursor: true,
    autoplay: {
        delay: 4500,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.option-pagination',
        type: 'bullets',
        clickable: true,
        // dynamicBullets: true,
    },
    breakpoints: {
        320: {
            slidesPerView: 1.2,
            spaceBetween: 8,
            centeredSlides: true,
            centeredSlidesBounds: true,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 40,
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 50,
        },
    },
})
const client_slider = new Swiper('.client-slider', {
    rtl: true,
    loop: false,
    grabCursor: true,
    autoplay: {
        delay: 4500,
        disableOnInteraction: false,
    },

    breakpoints: {
        320: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 40,
        },
        1024: {
            slidesPerView: 4,
            spaceBetween: 50,
        },
    },
})
const gallery_thumbnail = new Swiper(".gallery_thumbnail", {
    spaceBetween: 10,
    slidesPerView: 4,
    loop: true,
    loopedSlides: 4,
    rtl: true,
    slideToClickedSlide: true,
});
const gallery = new Swiper(".gallery_slider", {
    spaceBetween: 10,
    loop: false,
    rtl: true,
    loopedSlides: 4,
    thumbs: {
        swiper: gallery_thumbnail,
    },
});
const tst_slider = new Swiper(".tst_slider", {
    spaceBetween: 0,
    loop: true,
    rtl: true, autoplay: {
        delay: 4500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: ".tst-next",
        prevEl: ".tst-prev",
    },
});
const price_slider = new Swiper(".price_slider", {
    spaceBetween: 5,
    loop: true, grabCursor: true,
    rtl: true, autoplay: {
        delay: 4500,
        disableOnInteraction: false,
    },
    breakpoints: {
        320: {
            slidesPerView: 1.2,
            spaceBetween: 0, centeredSlides: false,
            centeredSlidesBounds: false,
        },
        350: {
            slidesPerView: 1.4,
            spaceBetween: 0,
            centeredSlides: false,
            centeredSlidesBounds: false,
        }, 480: {
            slidesPerView: 1.5,
            spaceBetween: 0,
            centeredSlides: false,
            centeredSlidesBounds: false,
        }, 530: {
            slidesPerView: 2,
            spaceBetween: 0,
            centeredSlides: false,
            centeredSlidesBounds: false,
        }, 650: {
            slidesPerView: 2.2,
            spaceBetween: 0,
            centeredSlides: true,
            centeredSlidesBounds: true,
        },
        880: {
            slidesPerView: 3,
            spaceBetween: 0, centeredSlides: true,
            centeredSlidesBounds: true,
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 5, centeredSlides: true,
            centeredSlidesBounds: true,
        },
    },
});

/***
 * Testimonials Animations
 */
const randomX = random(0, 20);
const randomY = random(0, 20);
const randomTime = random(1, 3);
const randomTime2 = random(1, 2);
const cans = gsap.utils.toArray('.tst_an');
const tl = gsap.timeline();

cans.forEach(can => {
    tl.set(can, {
        x: randomX(-1),
        y: randomX(1),
    }, 0);

    tl.add(moveX(can, 1), 0);
    tl.add(moveY(can, -1), 0);
    tl.repeat(-1);
    tl.yoyo(1);
});


function moveX(target, direction) {

    return gsap.to(target, randomTime(), {
        x: () => randomX(direction),
        ease: Sine.easeInOut,
        // onComplete: moveX,
        onCompleteParams: [target, direction * -1]
    });
}

function moveY(target, direction) {

    return gsap.to(target, randomTime2(), {
        y: () => randomY(direction),
        ease: Sine.easeInOut,
        // onComplete: moveY,
        onCompleteParams: [target, direction * -1]
    });
}

function random(min, max) {
    const delta = max - min;
    return (direction = 1) => (min + delta * Math.random()) * direction;
}

gsap.to(".sm-circle", 5, {
    y: 300,
    repeat: -1,
    yoyo: true,
    ease: 'none',
});
gsap.to(".sm-circle-2", 5, {
    y: -200,
    repeat: -1,
    yoyo: true,
    ease: 'none',
});


/***
 * Team Animations
 */


let animation = gsap.timeline()
animation.to(".circle-1", {rotation: 360, duration: 20, repeat: -1, ease: "none"})
    .to(".cris-1", {rotation: "-=360", duration: 20, repeat: -1, ease: "none"}, 0);
let animation_2 = gsap.timeline()
animation_2.to(".circle-2", {rotation: -360, duration: 18, repeat: -1, ease: "none"})
    .to(".cris-2", {rotation: "+=360", duration: 18, repeat: -1, ease: "none"}, 0);
let animation_3 = gsap.timeline()
animation_3.to(".circle-3", {rotation: 360, duration: 25, repeat: -1, ease: "none"})
    .to(".cris-3", {rotation: "-=360", duration: 25, repeat: -1, ease: "none"}, 0);


var collection = document.getElementsByClassName("circle-1");
collection[0].addEventListener("mouseover", function (e) {
    animation.pause();
    animation_2.pause();
    animation_3.pause();
});
collection[0].addEventListener("mouseout", function (e) {
    animation.play();
    animation_2.play();
    animation_3.play();
});
var collection2 = document.getElementsByClassName("circle-2");
collection2[0].addEventListener("mouseover", function (e) {
    animation.pause();
    animation_2.pause();
    animation_3.pause();
});
collection2[0].addEventListener("mouseout", function (e) {
    animation.play();
    animation_2.play();
    animation_3.play();
});
var collection3 = document.getElementsByClassName("circle-3");
collection3[0].addEventListener("mouseover", function (e) {
    animation.pause();
    animation_2.pause();
    animation_3.pause();
});
collection3[0].addEventListener("mouseout", function (e) {
    animation.play();
    animation_2.play();
    animation_3.play();
});

/***
 * Typing Effect
 */
const typedTextSpan = document.querySelector(".typed-text");
const cursorSpan = document.querySelector(".cursor");
const textArray = [" کسب و کار شما", "معرفی سازمان", "ارائه خدمات پزشکی", "معرفی شرکت تجاری"];
const typingDelay = 200;
const erasingDelay = 100;
const newTextDelay = 2000;
let textArrayIndex = 0;
let charIndex = 0;

function type() {
    if (charIndex < textArray[textArrayIndex].length) {
        if (!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
        typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, typingDelay);
    } else {
        cursorSpan.classList.remove("typing");
        setTimeout(erase, newTextDelay);
    }
}

function erase() {
    if (charIndex > 0) {
        if (!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
        typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(erase, erasingDelay);
    } else {
        cursorSpan.classList.remove("typing");
        textArrayIndex++;
        if (textArrayIndex >= textArray.length) textArrayIndex = 0;
        setTimeout(type, typingDelay + 1100);
    }
}

document.addEventListener("DOMContentLoaded", function () {
    if (textArray.length) setTimeout(type, newTextDelay + 250);
});

/***
 * popover & Tooltips
 *
 */
const list = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
list.map((el) => {
    let opts = {
        animation: true,
    }
    if (el.hasAttribute('data-bs-content-id')) {
        opts.content = document.getElementById(el.getAttribute('data-bs-content-id')).innerHTML;
        opts.html = true;
    }
    new bootstrap.Popover(el, opts);
});

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})
/***
 * counter
 */
var elements = document.getElementsByClassName("counts");
var elementsArr = Array.from(elements);
elementsArr.forEach(myFunction);

function myFunction(currentValue, index) {
    var count = currentValue,
        zero = {val: 0},
        num = count.getAttribute("data-number"),
        split = (num + "").split("."),
        decimals = split.length > 1 ? split[1].length : 0;
    gsap.to(zero, {
        val: num,
        duration: 3,
        scrollTrigger: currentValue,
        onUpdate: () => {
            count.innerText = zero.val.toFixed(decimals);
        }
    });
}

/***
 * Faq
 */
let btns = document.querySelectorAll('.accordion-button');
btns.forEach(
    (c) => c.onclick = (e) => {
        btns.forEach(
            (c) => c.parentElement.parentElement.classList[e.target == c ? 'toggle' : 'remove']('active')
        )
    }
)


/***
 * Animations
 */

function animateFrom(elem, direction) {
    direction = direction || 1;
    var x = 0,
        y = direction * 200;
    if (elem.classList.contains("gs_reveal_fromLeft")) {
        x = -200;
        y = 0;
    } else if (elem.classList.contains("gs_reveal_fromRight")) {
        x = 200;
        y = 0;
    }
    elem.style.transform = "translate(" + x + "px, " + y + "px)";
    elem.style.opacity = "0";
    gsap.fromTo(elem, {x: x, y: y, autoAlpha: 0}, {
        duration: 1.25,
        x: 0,
        y: 0,
        autoAlpha: 1,
        ease: "expo",
        overwrite: "auto"
    });
}


function hide(elem) {
    gsap.set(elem, {opacity: 0});
}

document.addEventListener("DOMContentLoaded", function () {
    gsap.registerPlugin(ScrollTrigger);

    gsap.utils.toArray(".gs_reveal").forEach(function (elem) {
        hide(elem); // assure that the element is hidden when scrolled into view

        ScrollTrigger.create({
            trigger: elem,
            // start: "top center",
            onEnter: function () {
                animateFrom(elem)
            },
            onEnterBack: function () {
                animateFrom(elem, -1)
            },
            onLeave: function () {
                hide(elem)
            } // assure that the element is hidden when scrolled into view
        });
    });
    gsap.to(".gs_scale", {
        scale: 1,
        ease: "expo",
        scrollTrigger: {
            trigger: ".gs_scale",
            // start: "top bottom", // the default values
            // end: "bottom top",
            scrub: true
        },
    });
    gsap.to(".cat-blg", {
        duration: 2,
        scale: 1,
        opacity: 1,
        delay: 0.5,
        stagger: .3,
        ease: "expo",
        force3D: true,
        scrollTrigger: {
            trigger: ".cat-blg",
            start: "center bottom", // the default values
            // end: "bottom top",
            scrub: true
        },
    });

    gsap.to(".gs_parallax", {
        yPercent: -50,
        ease: "none",
        scrollTrigger: {
            trigger: ".gs_parallax",
            start: "center bottom", // the default values
            // end: "bottom top",
            scrub: true
        },
    });

});

$(document).ready(function () {
    $('body').scrollspy({
        target: '#scroll-spy',
        offset: 70
    }).on('mouseenter mouseleave', '.nav-item', function (e) {
        if ($(window).width() > 750) {
            var _d = $(e.target).closest('.nav-item');
            _d.addClass('show');
            setTimeout(function () {
                _d[_d.is(':hover') ? 'addClass' : 'removeClass']('show');
            }, 1);
        }
    }).addClass("ct-render");
    $(window).scroll(function () {
        calcer();
    });
    calcer();

    function calcer() {
        if ($(window).scrollTop() > 500) {
            $('header').addClass('solid');
        } else {
            $('header').removeClass('solid');
        }
    }


    /***
     * Go to top
     */
    var progressPath = document.querySelector('.progress-wrap path');
    var pathLength = progressPath.getTotalLength();
    progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
    progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
    progressPath.style.strokeDashoffset = pathLength;
    progressPath.getBoundingClientRect();
    progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
    var updateProgress = function () {
        var scroll = $(window).scrollTop();
        var height = $(document).height() - $(window).height();
        var progress = pathLength - (scroll * pathLength / height);
        progressPath.style.strokeDashoffset = progress;
    }
    updateProgress();
    $(window).scroll(updateProgress);
    var offset = 50;
    var duration = 550;
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > offset) {
            $('.progress-wrap').addClass('active-progress');
        } else {
            $('.progress-wrap').removeClass('active-progress');
        }
    });
    $('.progress-wrap').on('click', function (event) {
        event.preventDefault();
        $('html, body').animate({scrollTop: 0}, duration);
        return false;
    })

    function submitForm() {
        let t = $("#name_input").val(),
            a = $("#phone_input").val(),
            e = $("#email_input").val(),
            n = $("#subject_input").val(),
            o = $("#message").val();
        let url = $("#contactForm").attr('action')
        $.ajax({
            type: "POST",
            url: url,
            data: {name: t, email: e, phone: a, subject: n, message: o},
            success: function (t) {
                "success" === t ? formSuccess() : (formError(), submitMSG(!1, t))
            }
        })
    }

    function formSuccess() {
        $("#contactForm")[0].reset(), submitMSG(!0, "پیام شما با موفقیت ارسال شد")

    }

    function formError() {
        $("#contactForm").addClass('form-error');
    }

    function submitMSG(t, a) {
        if (t) var e = "alert alert-success"; else e = "alert alert-danger";
        $("#msgSubmit").removeClass().addClass(e).text(a)
    }

    $("#contactForm").validator().on("submit", function (t) {

        if (t.isDefaultPrevented()) {
            formError()
        } else {
            (t.preventDefault(), submitForm())
        }

    })

   /**
     * Isotope
     */
    let qsRegex;
    let buttonFilters = {};
    let buttonFilter;
    let r = $(".portfolios").isotope({
        itemSelector: ".element-item",
        percentPosition: !0,
        originLeft: !1,
        layoutMode: "fitRows",
        filter: function () {
            var $this = $(this);
            var searchResult = qsRegex ? $this.text().match(qsRegex) : true;
            var buttonResult = buttonFilter ? $this.is(buttonFilter) : true;
            return searchResult && buttonResult;
        },
    });
    $(".f-b-g").on("click", "span", function () {
        buttonFilter = $(this).attr("data-filter");
        r.isotope();
        $(".f-b-g span").removeClass("active shadow"), $(this).addClass("active shadow")
    })


    /****
     * Customize
     */

    $('[data-color]').click(function () {
        $('body').removeClass().addClass($(this).attr('data-color'))
    });
    $('.thumb').click(function () {
        $('.customizer').toggleClass('ok')
    });
    $('#fonts-selector').change(function () {
        $('body').removeClass('shabnam iranyekan iransans vazir').addClass($(this).val())
    })
    TweenMax.to('.gear i', 2, {rotation: "+=360", repeat: -1, ease: Linear.easeNone, transformOrigin: "50% 50%"});
});

