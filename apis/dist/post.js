"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
class Post {
    constructor(textareaId, buttonId) {
        this.textarea = document.getElementById(textareaId);
        this.buttonPostId = document.getElementById(buttonId);
        this.textarea.addEventListener("input", () => this.updateButtonState());
        this.buttonPostId.addEventListener("click", () => this.sendPostData());
        this.updateButtonState();
    }
    updateButtonState() {
        const content = this.textarea.value.trim();
        this.buttonPostId.disabled = content.length === 0;
    }
    sendPostData() {
        return __awaiter(this, void 0, void 0, function* () {
            const content = this.textarea.value;
            const data = { content: content };
            try {
                const response = yield fetch('/api/send-post', {
                    method: "POST",
                    headers: {
                        'Content-Type': "application/json"
                    },
                    body: JSON.stringify(data)
                });
                this.textarea.value = '';
                location.reload();
            }
            catch (error) {
                console.error('Error:', error);
            }
        });
    }
}
document.addEventListener('DOMContentLoaded', () => {
    new Post("post-data", "post-btn");
});
