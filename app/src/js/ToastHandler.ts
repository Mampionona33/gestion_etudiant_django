import * as bootstrap from "bootstrap";

export enum ToastType {
    Error = 'error',
    Message = 'message',
    Info = 'info'
}

class ToastHandler {
    private message: string;
    private toastContainer: HTMLElement | null;
    private type: ToastType;

    constructor(message: string, type: ToastType = ToastType.Message) {
        this.message = message;
        this.toastContainer = null;
        this.type = type;
    }

    render() {
        // Créez un élément de toast en utilisant le DOM
        this.toastContainer = document.createElement('div');
        this.toastContainer.setAttribute('aria-live', 'polite');
        this.toastContainer.setAttribute('aria-atomic', 'true');
        this.toastContainer.style.position = 'fixed';
        this.toastContainer.style.bottom = '0px';
        this.toastContainer.style.right = '0px';
        this.toastContainer.style.zIndex = '9999';

        const toast = document.createElement('div');
        toast.className = `toast`;

        const toastHeader = document.createElement('div');
        toastHeader.className = `toast-header justify-content-between bg-${this.getToastBackgroundColor()} text-white` ;

        const toastHeaderRight = document.createElement('div');
        toastHeaderRight.className = 'd-flex'

        const strong = document.createElement('strong');
        strong.className = 'mr-auto';
        strong.textContent = this.getToastHeaderText();

        const small = document.createElement('small');
        small.textContent = 'Now';

        const closeButton = document.createElement('button');
        closeButton.type = 'button';
        closeButton.className = 'btn-close';
        closeButton.setAttribute('data-bs-dismiss', 'toast');
        closeButton.setAttribute('aria-label','Close')

        toastHeader.appendChild(strong);
        toastHeaderRight.appendChild(small)
        toastHeaderRight.appendChild(closeButton)
        toastHeader.appendChild(toastHeaderRight);

        const toastBody = document.createElement('div');
        toastBody.className = 'toast-body';
        toastBody.textContent = this.message;

        toast.appendChild(toastHeader);
        toast.appendChild(toastBody);

        this.toastContainer.appendChild(toast);

        closeButton.addEventListener('click', () => {
            this.hideToast();
        });

        // Ajoutez le toast au corps du document
        document.body.appendChild(this.toastContainer);

        // Créez une instance de la classe Bootstrap Toast et affichez le toast
        const toastInstance = new bootstrap.Toast(toast);
        toastInstance.show();

        // Supprimez automatiquement le toast après quelques secondes (par exemple, 5 secondes)
        setTimeout(() => {
            this.hideToast();
        }, 5000);
    }

    private hideToast() {
        if (this.toastContainer) {
            this.toastContainer.remove();
        }
    }

    private getToastBackgroundColor(): string {
        switch (this.type) {
            case ToastType.Error:
                return 'danger';
            case ToastType.Info:
                return 'info';
            default:
                return 'primary';
        }
    }

    private getToastHeaderText(): string {
        switch (this.type) {
            case ToastType.Error:
                return 'Erreur';
            case ToastType.Info:
                return 'Information';
            default:
                return 'Message';
        }
    }
}

export default ToastHandler;
