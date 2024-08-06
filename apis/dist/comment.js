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
class Comments {
    constructor(inputComment, sendCommentBtn, idp) {
        this.inputComment = inputComment;
        this.sendCommentBtn = sendCommentBtn;
        this.idp = idp;
        this.inputComment.addEventListener('input', () => this.updateButtonState());
        this.sendCommentBtn.addEventListener('click', () => this.sendCommentData());
        this.updateButtonState();
    }
    updateButtonState() {
        const content = this.inputComment.value.trim();
        this.sendCommentBtn.disabled = content.length === 0;
    }
    sendCommentData() {
        return __awaiter(this, void 0, void 0, function* () {
            const content = this.inputComment.value;
            const postId = this.idp.textContent;
            const data = { content: content, post_id: postId };
            try {
                const response = yield fetch("/api/send-comment", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });
                this.inputComment.value = '';
                this.updateButtonState();
                location.reload();
            }
            catch (error) {
                console.error("Error: ", error);
            }
        });
    }
}
document.addEventListener("DOMContentLoaded", () => {
    const inputComments = document.querySelectorAll('.commentContent');
    const sendCommentBtns = document.querySelectorAll('.sendComment');
    const idps = document.querySelectorAll('.idp');
    inputComments.forEach((input, index) => {
        const button = sendCommentBtns[index];
        const idp = idps[index];
        new Comments(input, button, idp);
    });
});
