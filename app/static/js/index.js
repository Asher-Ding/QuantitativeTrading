function showSuccessMessage() {
    var successMessageBox = document.getElementById("success-message");
    successMessageBox.classList.remove("hidden");

    setTimeout(hideSuccessMessage, 3000); // 隐藏弹窗，时间设定为 3 秒
}

function hideSuccessMessage() {
    var successMessageBox = document.getElementById("success-message");
    successMessageBox.classList.add("hidden");
}
