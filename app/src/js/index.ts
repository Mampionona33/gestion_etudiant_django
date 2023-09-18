import "../styles/style.scss";
import ToastHandler,{ ToastType } from './ToastHandler.ts';
import * as bootstrap from "bootstrap";

document.addEventListener('DOMContentLoaded', function () {
    // Récupérez la valeur de error_message de manière appropriée, par exemple en l'ajoutant comme attribut data dans un élément HTML
    const error_message = document.getElementById('error-message');
    if(error_message){
        const error_message_content = error_message.getAttribute('data-error-message');
        if(error_message_content){
            const toastHandlerError = new ToastHandler(error_message_content,ToastType.Error); 
            toastHandlerError.render();
        }
    }
    
});