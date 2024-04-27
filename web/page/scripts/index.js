gsap.registerPlugin(ScrollTrigger, ScrollSmoother);

if (ScrollTrigger.isTouch !== 1) {
    ScrollSmoother.create({
        wrapper: ".wrapper",
        content: ".content",
        smooth: 1.5, 
        effects: true
    });

    gsap.fromTo(".mainlogo", { opacity: 1 }, {
        opacity: 0,
        scrollTrigger: {
            trigger: ".mainlogo",
            start: "100",
            end: "300",
            scrub: true
        }
    });
    
    gsap.fromTo(".welcome", { opacity: 0 }, {
        opacity: 1,
        scrollTrigger: {
            trigger: ".welcome",
            scrub: true
        }
    });

    gsap.fromTo(".whatiskeymasters", { x: -500 }, {
        x: 0,
        scrollTrigger: {
            trigger: ".mainlogo",
            scrub: true
        }
    });
    
    gsap.fromTo(".welcome", { opacity: 1 }, {
        opacity: 0,
        scrollTrigger: {
            trigger: ".KeymastersPasswords",
            scrub: true
        }
    });

    gsap.fromTo(".KeymastersPasswords", { opacity: 0 }, {
        opacity: 1,
        scrollTrigger: {
            trigger: ".KeymastersPasswords",
            scrub: true
        }
    });

    gsap.fromTo("#KPLogo", { x: 500 }, {
        x: 0,
        scrollTrigger: {
            trigger: ".welcome",
            scrub: true
        }
    });
    
    gsap.fromTo(".KeymastersPasswords", { opacity: 1 }, {
        opacity: 0,
        scrollTrigger: {
            trigger: ".KeymastersVault",
            scrub: true
        }
    });

    gsap.fromTo(".KeymastersVault", { opacity: 0 }, {
        opacity: 1,
        scrollTrigger: {
            trigger: ".KeymastersVault",
            scrub: true
        }
    });

    gsap.fromTo(".what-is-KV", { x: -500 }, {
        x: 0,
        scrollTrigger: {
            trigger: ".KeymastersPasswords",
            scrub: true
        }
    });
    
    gsap.fromTo(".KeymastersVault", { opacity: 1 }, {
        opacity: 0,
        scrollTrigger: {
            trigger: ".KeymastersCrypto",
            scrub: true
        }
    });

    gsap.fromTo(".KeymastersCrypto", { opacity: 0 }, {
        opacity: 1,
        scrollTrigger: {
            trigger: ".KeymastersVault",
            scrub: true
        }
    });

    gsap.fromTo("#KCLogo", { x: 500 }, {
        x: 0,
        scrollTrigger: {
            trigger: ".KeymastersVault",
            scrub: true
        }
    });
    
    gsap.fromTo(".KeymastersCrypto", { opacity: 1 }, {
        opacity: 0,
        scrollTrigger: {
            trigger: ".KeymastersSCAMGuard",
            scrub: true
        }
    });
}