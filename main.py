from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()
client = OpenAI()

class Book(BaseModel):
    bookId: int
    content: str

class BookDetail(BaseModel):
    bookId: int

@app.post("/test")
def test(books: list[Book]):

    data = []

    for book in books:  # Fix 1: Loop through books directly
        j = hi(book)

        if j == 1:
            book_detail_data = {"bookId": book.bookId}
            book_detail = BookDetail(**book_detail_data)
            data.append(book_detail.dict())

    spring_server_url = "http://localhost:9039/hi/test"  # Spring 서버의 URL로 변경
    print(data)
    response = requests.get(spring_server_url, json={"data": data})

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to send data to Spring server")



def hi(book: Book):  # Fix 2: Use 'book' instead of 'Book'
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": book.content + " 이 문장이 유해한 단어나 욕설을 포함한다면, 0을 출력해줘 다른 이상한 말은 석지말고, 유해한 단어나 욕설이 없다면 1을 출력해줘 다른 이상한 말은 석지말고, 제발 숫자만 출력해줘 답변에 숫자만 출력해라"}
        ]
    )

    message = completion.choices[0].message
    print(message)
    value = int(message.content)
    print(value)
    return value
