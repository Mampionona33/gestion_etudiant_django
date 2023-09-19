import $ from "jquery";

export enum AlertType {
  Primary = "primary",
  Secondary = "secondary",
  Success = "success",
  Danger = "danger",
  Warning = "warning",
  Info = "info",
}

export default class AlertHandler {
  private callerId: JQuery<HTMLElement> | null;
  private message: string;
  private alertPlaceHolder: JQuery<HTMLElement> | null;
  private wrapper: HTMLElement | null;
  private type: AlertType;

  constructor(
    callerId: string,
    idTarget: string,
    message: string,
    type: AlertType
  ) {
    this.callerId = $(`*[id*=${callerId}]`);
    this.message = message;
    this.type = type;

    console.log(callerId); //output : btn-delete11
    console.log(this.callerId.get(0)?.id); // output : undefined ???

    this.alertPlaceHolder = $(`*[id*='${idTarget}']`);

    this.wrapper = null;
  }

  private createAlert() {
    this.wrapper = document.createElement("div");
    this.wrapper.innerHTML = `
    <div class="alert alert-${this.type} alert-dismissible" role="alert">
        <div>${this.message}</div>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    `;
  }

  render() {
    if (this.callerId) {
      console.log("test");
      this.createAlert();

      this.callerId.on("click", () => {
        console.log("test");
        if (this.alertPlaceHolder && this.wrapper) {
          this.alertPlaceHolder.append(this.wrapper);
        }
      });
    }
  }
}
