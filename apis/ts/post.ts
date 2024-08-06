class Post {
  private textarea: HTMLTextAreaElement;
  private buttonPostId: HTMLButtonElement;

  constructor(textareaId: string, buttonId: string) {
    this.textarea = document.getElementById(textareaId) as HTMLTextAreaElement;
    this.buttonPostId = document.getElementById(buttonId) as HTMLButtonElement;

    this.textarea.addEventListener("input", () => this.updateButtonState());
    this.buttonPostId.addEventListener("click", () => this.sendPostData());

    this.updateButtonState();
  }
  private updateButtonState() {
    const content = this.textarea.value.trim();
    this.buttonPostId.disabled = content.length === 0;
  }
  private async sendPostData() {
    const content = this.textarea.value;
    const data = {content: content};
    try {
      const response = await fetch('/api/send-post', {
        method: "POST",
        headers: {
          'Content-Type': "application/json"
        },
        body: JSON.stringify(data)
      });
      this.textarea.value = '';
      location.reload();
    } catch (error) {
      console.error('Error:', error);
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new Post("post-data", "post-btn");
})