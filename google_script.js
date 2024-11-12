function getHomes() {
  const url =
    "https://soco.seoul.go.kr/youth/pgm/home/yohome/bbsListJson.json?bbsId=BMSR00015&pageIndex=1";

  const options = {
    method: "post",
    headers: {
      "user-agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    },
  };

  const response = UrlFetchApp.fetch(url, options);
  const resJson = JSON.parse(response.getContentText());
  const resultList = resJson.resultList || [];

  const announcements = resultList.map((item) => ({
    공고명: item.nttSj,
    모집시작일: item.optn1,
    모집마감일: item.optn4,
  }));

  const today = Utilities.formatDate(new Date(), "Asia/Seoul", "yyyy-MM-dd");

  const hasTodayDate = announcements.some(
    (row) => row.모집시작일 === today || row.모집마감일 === today
  );
  if (hasTodayDate) {
    const recipient = "your-email@example.com"; //본인 이메일로 수정
    const subject = "당일 청년 주택 모집 공고 발생 🔥";
    let body = "공고 내용:\n\n";
    announcements.forEach((item) => {
      body += `공고명: ${item.공고명}\n모집시작일: ${item.모집시작일}\n모집마감일: ${item.모집마감일}\n\n`;
    });
    MailApp.sendEmail(recipient, subject, body);
  }
}
