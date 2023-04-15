// Obtener el formulario y el botón "Volver al inicio de sesión"
const passwordResetForm = document.querySelector('#password-reset-form');
const backToLoginButton = document.querySelector('#back-to-login');

// Agregar un controlador de eventos para el envío del formulario
passwordResetForm.addEventListener('submit', function(event) {
  // Prevenir el envío del formulario
  event.preventDefault();
  
  // Obtener el correo electrónico del usuario
  const email = document.querySelector('#email').value;
  
  // Validar que se ingresó un correo electrónico válido
  if (!email || !email.trim() || !validateEmail(email)) {
    alert('Por favor, ingrese un correo electrónico válido.');
    return;
  }
  
  // TODO: Enviar solicitud de recuperación de contraseña al servidor
  
  // Mostrar mensaje de éxito
  alert(`Se ha enviado un correo electrónico de recuperación de contraseña a ${email}.`);
  
  // Limpiar el formulario
  passwordResetForm.reset();
});

// Agregar un controlador de eventos para el botón "Volver al inicio de sesión"
backToLoginButton.addEventListener('click', function(event) {
  // Prevenir el comportamiento predeterminado del enlace
  event.preventDefault();
  
  // Redirigir al usuario a la página de inicio de sesión
  window.location.href = 'login.html';
});

// Función para validar un correo electrónico
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
