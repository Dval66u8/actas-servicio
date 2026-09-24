# ADR-001: Protección de actas guardadas en el celular

- **Fecha:** 23/09/2026
- **Estado:** Aceptado

## Contexto

Teníamos un problema con la seguridad de los datos personales de los clientes en caso de que el teléfono del técnico fuera robado, se perdiera o no volviera a conectarse nunca a internet, y debíamos definir cómo proceder en cada caso.

## Decisión

Decidimos implementar 5 capas de seguridad como medida de prevención ante cualquier posible caso.

1. **Cola de envío con prioridad:** los datos críticos salen con la primera señal; las fotos, después y por partes.
   **¿Por qué?** Para no perder la información más importante de las actas de servicio. Enviar rápido no solo evita perder el trabajo, también reduce la cantidad de datos de clientes guardados en el celular. Menos datos en el teléfono significa menos riesgo si lo roban.

2. **Cifrado en reposo:** lo que queda en el celular es ilegible.
   **¿Por qué?** Si alguien logra acceder al contenido del teléfono, no podrá leer la información, ya que estará cifrada a menos que el técnico se autentique.

3. **Llave protegida en el chip de seguridad, liberada solo con autenticación.**
   **¿Por qué?** La llave que descifra las actas nunca sale del chip de seguridad del celular y solo se usa cuando el técnico se autentica. Así, aunque alguien copie los archivos del teléfono, no podrá leerlos.

4. **Bloqueo de la app con biometría o PIN.**
   **¿Por qué?** El técnico necesitará su PIN o sus datos biométricos para usar la aplicación, que además se bloqueará sola tras unos minutos sin uso. La aplicación también bloqueará las capturas y grabaciones de pantalla. Estos serán los métodos principales de ingreso y protección de la aplicación.

5. **Borrado remoto como respaldo.**
   **¿Por qué?** Como último método de defensa, el administrador podrá marcar el teléfono del técnico como robado. Esto enviará una orden a la aplicación para eliminar todos los datos que tenga almacenados.

## Consecuencias

### Qué ganamos

Protegemos los datos personales de nuestros clientes y reducimos al mínimo los malentendidos causados por actas de servicio que no se alcanzaron a guardar.

### Qué cuesta

- Si el teléfono no vuelve a recibir señal por cualquier motivo, las actas que no se alcanzaron a enviar se pierden. Procuramos que esto ocurra la menor cantidad de veces posible.
- Si el técnico olvida su PIN y no tiene datos biométricos registrados, deberá pasar por una verificación exhaustiva de su identidad. Si no es posible verificarla, deberá restaurar la aplicación, perdiendo las actas no enviadas, para garantizar la protección de los datos de los clientes.
- Estas capas hacen la aplicación más compleja de construir y de probar.

### Límites

- Si roban el teléfono mientras el técnico está creando un acta de servicio con la aplicación abierta, esta se bloqueará tras unos minutos de inactividad y pedirá nuevamente el PIN o los datos biométricos. Durante esos minutos, quien tenga el celular podrá ver el acta abierta.
- Si el celular robado nunca se reconecta, el borrado remoto no llega, aunque los datos siguen cifrados.
- Si el técnico decide compartir información de los clientes, la aplicación bloquea las capturas de pantalla, pero no puede evitar que tome fotos con otro dispositivo. Ese riesgo se cubre con registro de auditoría y responsabilidad legal (ver ADR-002, pendiente).