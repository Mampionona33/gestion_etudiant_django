import "../styles/style.scss";
import AlertHandler, { AlertType } from "./AlertHandler.ts";
import ToastHandler, { ToastType } from "./ToastHandler.ts";
import * as bootstrap from "bootstrap";

const alertDelete = new AlertHandler(
  "btn-delete11",
  "delete",
  "Êtes-vous sûr de vouloir supprimer cette classe",
  AlertType.Danger
);

document.addEventListener("DOMContentLoaded", function () {
  // Récupérez la valeur de error_message de manière appropriée, par exemple en l'ajoutant comme attribut data dans un élément HTML
  const error_message = document.getElementById("error-message");
  if (error_message) {
    const error_message_content =
      error_message.getAttribute("data-error-message");
    if (error_message_content) {
      const toastHandlerError = new ToastHandler(
        error_message_content,
        ToastType.Error
      );
      toastHandlerError.render();
    }
  }

  const message_info = document.getElementById("message-info");
  if (message_info) {
    const message_info_content =
      error_message?.getAttribute("data-message-info");
    if (message_info_content) {
      const toastHandleMessageInfo = new ToastHandler(
        message_info_content,
        ToastType.Info
      );
      toastHandleMessageInfo.render();
    }
  }

  alertDelete.render();
});
