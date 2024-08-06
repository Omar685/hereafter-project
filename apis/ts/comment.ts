class Comments {
  private inputComment: HTMLInputElement;
  private sendCommentBtn: HTMLButtonElement;
  private idp: HTMLParagraphElement;

  constructor (inputComment: HTMLInputElement, sendCommentBtn: HTMLButtonElement, idp: HTMLParagraphElement) {
    this.inputComment = inputComment;
    this.sendCommentBtn = sendCommentBtn;
    this.idp = idp;

    this.inputComment.addEventListener('input', () => this.updateButtonState());
    this.sendCommentBtn.addEventListener('click', () => this.sendCommentData());

    this.updateButtonState();
  }

  private updateButtonState() {
    const content = this.inputComment.value.trim();
    this.sendCommentBtn.disabled = content.length === 0;
  }

  private async sendCommentData() {
    const content = this.inputComment.value;
    const postId = this.idp.textContent;
    const data = { content: content, post_id: postId };

    try {
      const response = await fetch("/api/send-comment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });
      this.inputComment.value = '';
      this.updateButtonState();
      location.reload();
    } catch (error) {
      console.error("Error: ", error);
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const inputComments = document.querySelectorAll('.commentContent');
  const sendCommentBtns = document.querySelectorAll('.sendComment');
  const idps = document.querySelectorAll('.idp');

  inputComments.forEach((input, index) => {
    const button = sendCommentBtns[index] as HTMLButtonElement;
    const idp = idps[index] as HTMLParagraphElement;
    new Comments(input as HTMLInputElement, button, idp);
  })
})