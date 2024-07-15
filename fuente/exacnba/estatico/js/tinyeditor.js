!(function () {
    "use strict";
    function d(e, t) {
        (null == t || t > e.length) && (t = e.length);
        for (var n = 0, r = new Array(t); n < t; n++) r[n] = e[n];
        return r;
    }
    function g(e, t) {
        var n = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
        if (!n) {
            if (
                Array.isArray(e) ||
                (n = (function (e, t) {
                    if (e) {
                        if ("string" == typeof e) return d(e, t);
                        var n = Object.prototype.toString.call(e).slice(8, -1);
                        return "Object" === n && e.constructor && (n = e.constructor.name), "Map" === n || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? d(e, t) : void 0;
                    }
                })(e)) ||
                (t && e && "number" == typeof e.length)
            ) {
                n && (e = n);
                var r = 0,
                    a = function () {};
                return {
                    s: a,
                    n: function () {
                        return r >= e.length ? { done: !0 } : { done: !1, value: e[r++] };
                    },
                    e: function (e) {
                        throw e;
                    },
                    f: a,
                };
            }
            throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
        }
        var l,
            i = !0,
            o = !1;
        return {
            s: function () {
                n = n.call(e);
            },
            n: function () {
                var e = n.next();
                return (i = e.done), e;
            },
            e: function (e) {
                (o = !0), (l = e);
            },
            f: function () {
                try {
                    i || null == n.return || n.return();
                } finally {
                    if (o) throw l;
                }
            },
        };
    }
    var v = "beforeend",
        u = "__toolbar-item",
        s = function (t, e, n, r) {
            var a = document.createElement("select");
            (a.dataset.commandId = t),
                (a.className = u),
                (a.title = e),
                a.addEventListener("change", function (e) {
                    return r(t, e.target.options[e.target.selectedIndex].value);
                });
            var l,
                i,
                o,
                d,
                s,
                m = g(n);
            try {
                for (m.s(); !(l = m.n()).done; ) {
                    var c = l.value;
                    a.insertAdjacentElement(v, ((i = c.value), (o = c.text), (d = c.selected), (s = void 0), ((s = document.createElement("option")).innerText = o), i && s.setAttribute("value", i), d && s.setAttribute("selected", d), s));
                }
            } catch (e) {
                m.e(e);
            } finally {
                m.f();
            }
            return a;
        },
        m = function (e, t, n, r) {
            var a = document.createElement("button");
            return (
                (a.dataset.commandId = e),
                (a.className = u),
                (a.title = t),
                (a.type = "button"),
                a.insertAdjacentElement(v, n),
                a.addEventListener("click", function () {
                    return r(e);
                }),
                a
            );
        },
        c = function (e) {
            var t = document.createElement("i");
            return (t.className = e), t;
        },
        h = "no",
        f = function () {
            var e = document.createElement("span");
            return (e.className = "__toolbar-separator"), e;
        },
        r = function (e, t) {
            var n,
                r,
                a,
                l,
                i,
                o = document.createElement("div");
            return (
                (o.className = "__toolbar"),
                e.formatblock !== h &&
                    o.insertAdjacentElement(
                        v,
                        s(
                            "formatblock",
                            "Styles",
                            [
                                { value: "h1", text: "Title 1" },
                                { value: "h2", text: "Title 2" },
                                { value: "h3", text: "Title 3" },
                                { value: "h4", text: "Title 4" },
                                { value: "h5", text: "Title 5" },
                                { value: "h6", text: "Title 6" },
                                { value: "p", text: "Paragraph", selected: !0 },
                                { value: "pre", text: "Preformatted" },
                            ],
                            t
                        )
                    ),
                e.fontname !== h &&
                    o.insertAdjacentElement(
                        v,
                        s(
                            "fontname",
                            "Font",
                            [
                                { value: "serif", text: "Serif", selected: !0 },
                                { value: "sans-serif", text: "Sans Serif" },
                                { value: "monospace", text: "Monospace" },
                                { value: "cursive", text: "Cursive" },
                                { value: "fantasy", text: "Fantasy" },
                            ],
                            t
                        )
                    ),
                e.bold !== h && o.insertAdjacentElement(v, m("bold", "Bold", c("tes te-bold"), t)),
                e.italic !== h && o.insertAdjacentElement(v, m("italic", "Italic", c("tes te-italic"), t)),
                e.underline !== h && o.insertAdjacentElement(v, m("underline", "Underline", c("tes te-underline"), t)),
                e.forecolor !== h &&
                    o.insertAdjacentElement(
                        v,
                        ((n = "forecolor"),
                        (r = "Text color"),
                        (a = "color"),
                        (l = t),
                        ((i = document.createElement("input")).dataset.commandId = n),
                        (i.className = u),
                        (i.title = r),
                        (i.type = a),
                        i.addEventListener("change", function (e) {
                            return l(n, e.target.value);
                        }),
                        i)
                    ),
                o.insertAdjacentElement(v, f()),
                e.justifyleft !== h && o.insertAdjacentElement(v, m("justifyleft", "Left align", c("tes te-align-left"), t)),
                e.justifycenter !== h && o.insertAdjacentElement(v, m("justifycenter", "Center align", c("tes te-align-center"), t)),
                e.justifyright !== h && o.insertAdjacentElement(v, m("justifyright", "Right align", c("tes te-align-right"), t)),
                o.insertAdjacentElement(v, f()),
                e.insertorderedlist !== h && o.insertAdjacentElement(v, m("insertorderedlist", "Numbered list", c("tes te-list-ol"), t)),
                e.insertunorderedlist !== h && o.insertAdjacentElement(v, m("insertunorderedlist", "Bulleted list", c("tes te-list-ul"), t)),
                e.outdent !== h && o.insertAdjacentElement(v, m("outdent", "Decrease indent", c("tes te-indent fa-flip-horizontal"), t)),
                e.indent !== h && o.insertAdjacentElement(v, m("indent", "Increase indent", c("tes te-indent"), t)),
                o.insertAdjacentElement(v, f()),
                e.removeFormat !== h && o.insertAdjacentElement(v, m("removeFormat", "Clear formatting", c("tes te-eraser"), t)),
                o
            );
        },
        e = function (n) {
            n.setAttribute("contentEditable", !0), (n.className = "__editor");
            var e = function (e, t) {
                document.execCommand(e, !1, t), n.focus();
            };
            e("defaultParagraphSeparator", "p");
            var f = r(n.dataset, e);
            n.insertAdjacentElement("beforebegin", f);
            var t = function () {
                var r,
                    t = g(f.querySelectorAll("select[data-command-id]"));
                try {
                    var e = function () {
                        var e = r.value,
                            t = document.queryCommandValue(e.dataset.commandId),
                            n = Array.from(e.options).find(function (e) {
                                return e.value === t;
                            });
                        e.selectedIndex = n ? n.index : -1;
                    };
                    for (t.s(); !(r = t.n()).done; ) e();
                } catch (e) {
                    t.e(e);
                } finally {
                    t.f();
                }
                var n,
                    a = g(f.querySelectorAll("button[data-command-id]"));
                try {
                    for (a.s(); !(n = a.n()).done; ) {
                        var l = n.value,
                            i = document.queryCommandState(l.dataset.commandId);
                        l.classList.toggle("active", i);
                    }
                } catch (e) {
                    a.e(e);
                } finally {
                    a.f();
                }
                var o,
                    d,
                    s,
                    m,
                    c,
                    v = g(f.querySelectorAll("input[data-command-id]"));
                try {
                    for (v.s(); !(o = v.n()).done; ) {
                        var u = o.value,
                            h = document.queryCommandValue(u.dataset.commandId);
                        u.value = ((c = void 0), (d = /(.*?)rgb\((\d+), (\d+), (\d+)\)/.exec(h)), (s = parseInt(d[2])), (m = parseInt(d[3])), (c = parseInt(d[4]) | (m << 8) | (s << 16)), d[1] + "#" + c.toString(16).padStart(6, "0"));
                    }
                } catch (e) {
                    v.e(e);
                } finally {
                    v.f();
                }
            };
            n.addEventListener("keydown", t), n.addEventListener("keyup", t), n.addEventListener("click", t), f.addEventListener("click", t);
        };
    !(function (e, t) {
        void 0 === t && (t = {});
        var n = t.insertAt;
        if (e && "undefined" != typeof document) {  
            var r = document.head || document.getElementsByTagName("head")[0],
                a = document.createElement("style");
            (a.type = "text/css"), "top" === n && r.firstChild ? r.insertBefore(a, r.firstChild) : r.appendChild(a), a.styleSheet ? (a.styleSheet.cssText = e) : a.appendChild(document.createTextNode(e));
        }
    })(
        ".__editor {\n  background: #transparent;\n  border: solid 1px #e0e0e0;\n  color: var(--color-blanco-paloma-mia);\n  font-family: 'serif';\n  margin-top: 10px;\n  overflow: scroll;\n  padding: 10px;\n}\n\n.__editor:focus {\n  outline: none;\n}\n\n.__toolbar {\n  display: flex;\n  flex-wrap: wrap;\n  padding: 5px;\n}\n\n.__toolbar-item {\n  background: #transparent;\n  border: 0;\n ;\n  cursor: pointer;\n  margin-right: 7px;\n  min-width: 30px;\n  padding: 5px;\n}\n\n.__toolbar-item:hover,\n.__toolbar-item.active {\n  background: var(--color-yuyo-verde);\n}\n\n.__toolbar-separator {\n  border-left: solid 1px #e0e0e0;\n  margin-right: 7px;\n}\n\n.__toolbar-separator:last-child {\n  display: none;\n}\n\n.tes{\n\tfont-style: normal; color:var(--color-blanco-paloma-mia);\n}\n\n.te-bold::before {\n\n\tcolor:var(--color-blanco-paloma-mia);\tcontent: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M6.8 19V5h5.525q1.625 0 3 1T16.7 8.775q0 1.275-.575 1.963t-1.075.987q.625.275 1.388 1.025T17.2 15q0 2.225-1.625 3.113t-3.05.887zm3.025-2.8h2.6q1.2 0 1.463-.612t.262-.888t-.262-.887t-1.538-.613H9.825zm0-5.7h2.325q.825 0 1.2-.425t.375-.95q0-.6-.425-.975t-1.1-.375H9.825z'/%3E%3C/svg%3E\");\n\tfont-weight: bold;\n}\n\n.te-italic::before {\n\tcontent: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M5 19v-2.5h4l3-9H8V5h10v2.5h-3.5l-3 9H15V19z'/%3E%3C/svg%3E\");\n\tfont-style: italic;\n}\n\n.te-underline::before {\n\tcontent: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M5 21v-2h14v2zm7-4q-2.525 0-3.925-1.575t-1.4-4.175V3H9.25v8.4q0 1.4.7 2.275t2.05.875t2.05-.875t.7-2.275V3h2.575v8.25q0 2.6-1.4 4.175T12 17'/%3E%3C/svg%3E\");\n\ttext-decoration: underline;\n}\n\n.te-align-left::before {\n\tcontent: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M3 21v-2h18v2zm0-4v-2h12v2zm0-4v-2h18v2zm0-4V7h12v2zm0-4V3h18v2z'/%3E%3C/svg%3E\");\n}\n\n.te-align-center::before {\n\tcontent: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M3 21v-2h18v2zm4-4v-2h10v2zm-4-4v-2h18v2zm4-4V7h10v2zM3 5V3h18v2z'/%3E%3C/svg%3E\");\n}\n\n.te-align-right::before {\n\tcontent: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M3 5V3h18v2zm6 4V7h12v2zm-6 4v-2h18v2zm6 4v-2h12v2zm-6 4v-2h18v2z'/%3E%3C/svg%3E\");\n}\n\n.te-list-ol::before {\n\tcontent: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M3 22v-1.5h2.5v-.75H4v-1.5h1.5v-.75H3V16h3q.425 0 .713.288T7 17v1q0 .425-.288.713T6 19q.425 0 .713.288T7 20v1q0 .425-.288.713T6 22zm0-7v-2.75q0-.425.288-.712T4 11.25h1.5v-.75H3V9h3q.425 0 .713.288T7 10v1.75q0 .425-.288.713T6 12.75H4.5v.75H7V15zm1.5-7V3.5H3V2h3v6zM9 19v-2h12v2zm0-6v-2h12v2zm0-6V5h12v2z'/%3E%3C/svg%3E\");\n}\n\n.te-list-ul::before {\n\tcontent:url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M9 19v-2h12v2zm0-6v-2h12v2zm0-6V5h12v2zM5 20q-.825 0-1.412-.587T3 18t.588-1.412T5 16t1.413.588T7 18t-.587 1.413T5 20m0-6q-.825 0-1.412-.587T3 12t.588-1.412T5 10t1.413.588T7 12t-.587 1.413T5 14m0-6q-.825 0-1.412-.587T3 6t.588-1.412T5 4t1.413.588T7 6t-.587 1.413T5 8'/%3E%3C/svg%3E\");\n\twhite-space: pre-wrap;\n\tdisplay:inline-block;\n\tline-height: 0.5;\n}\n\n.te-indent::before {\n\tcontent:url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='M3 21v-2h18v2zm8-4v-2h10v2zm0-4v-2h10v2zm0-4V7h10v2zM3 5V3h18v2zm0 11V8l4 4z'/%3E%3C/svg%3E\");\n\twhite-space: pre-wrap;\n\tdisplay:inline-block;\n\tline-height: 0.5;\n}\n\n.te-indent.te-flip-horizontal::before {\n\ttransform: rotate(180deg);\n}\n\n.te-eraser::before {\n\tcontent:url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 24 24'%3E%3Cpath fill='white' d='m13.2 10.35l-2.325-2.325L7.85 5H20v3h-5.8zm6.6 12.25l-8.3-8.3l-2 4.7H6.225L9.2 12L1.4 4.2l1.4-1.4l18.4 18.4z'/%3E%3C/svg%3E\");\n\twhite-space: pre-wrap;\n\tdisplay:inline-block;\n\tline-height: 0.5;\n}"
    ),
        document.querySelectorAll("[data-tiny-editor]").forEach(e),
        (window.__tinyEditor = { transformToEditor: e });
})();

function escaparHTML (inseguro){
    return inseguro
        .replace('<script>.*</script>','')
        .replace(`/&/g`, "&amp;")
        .replace(`/</g`, "&lt;")
        .replace(`/>/g`, "&gt;")    
        .replace(`/"/g`, "&quot;")
        .replace(`/'/g`, "&#039;")
        .replace(`/'/g`, "&#039;")
        .replace(`/'/g`, "&#039;");
}

document.querySelectorAll('.__editor').forEach(e =>{e.addEventListener('paste', function (event) {
    event.preventDefault();
    event.target.innerText = event.clipboardData.getData("text/plain");
});})
//# sourceMappingURL=bundle.js.map
