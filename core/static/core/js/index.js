const form = document.getElementById('registro');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const nombre = document.getElementById('nombre').value.trim();
  const usuario = document.getElementById('usuario').value.trim();
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value;
  const password2 = document.getElementById('password2').value;
  const phone = document.getElementById('phone').value;
  const direccion = document.getElementById('direccion').value.trim();

  // Validación de campos requeridos
  if (!nombre || !usuario || !email || !password || !password2 || !phone) {
    alert('Por favor, complete todos los campos requeridos');
    return;
  }

  // Validación de formato de correo electrónico
  if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
    alert('Por favor, ingrese un correo electrónico válido');
    return;
  }

  // Validación de contraseñas iguales
  if (password !== password2) {
    alert('Las contraseñas no coinciden');
    return;
  }

  // Validación de número de teléfono
  if (!/^[0-9]{9}$/.test(phone)) {
    alert('Por favor, ingrese un número de teléfono válido (solo números)');
    return;
  }

  // Validación de contraseña
  if (!/(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,18}/.test(password)) {
    alert('La contraseña debe tener al menos una letra mayúscula, una letra minúscula, un número y tener entre 6 y 18 caracteres');
    return;
  }

  // Si llegamos hasta aquí, todo está validado correctamente
  alert('Formulario enviado correctamente');
  form.reset();
});