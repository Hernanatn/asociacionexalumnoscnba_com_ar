function mostrarContrasena() {
    var x = document.getElementById("caja-contrasena");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
    var y = document.getElementById("caja-repetir-contrasena");
    if (y.type === "password") {
      y.type = "text";
    } else {
      y.type = "password";
    }

    htmx.findAll('.ojo').forEach(
      (elemento) => {
          htmx.toggleClass(elemento,"")
          elemento.remove();
      }
  );
  }

const cargarImagen = (image) => {
    image.setAttribute("src", image.getAttribute("data-src"));
    image.onload = () => {
        image.removeAttribute("data-src");
        };
    };

    const cargarSet = (image) => {
    image.setAttribute("srcset", image.getAttribute("data-src-set"));
    image.onload = () => {
        image.removeAttribute("data-src-set");
        };
    };

    function procesarImagenesRestantes(){
        const imagenesRestantes = document.querySelectorAll("img[data-src]");
        imagenesRestantes.forEach(
            (e,i) => {
                setTimeout(
                    () => {cargarImagen(e);},
                    i * 35
                )
            }
        );
        const setRestantes = document.querySelectorAll("img[data-src-set]");
        setRestantes.forEach(
            (e,i) => {
                setTimeout(
                    () => {cargarSet(e);},
                    i * 35
                )
            }
        );
    }

    procesarImagenesRestantes();

    window.setInterval(
        procesarImagenesRestantes,
        2750
    )
