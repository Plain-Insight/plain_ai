const express = require('express');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const { GoogleGenerativeAI } = require('@google/generative-ai');

const app = express();
const PORT = process.env.PORT || 3000;

// 미들웨어 설정
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Google Generative AI 설정
const genAI = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash-lite" });

// 채팅 세션 저장을 위한 Map (실제 서비스에서는 데이터베이스 사용 권장)
const chatSessions = new Map();

// 루트 라우트 - index.html 제공
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// 새로운 채팅 세션 시작
app.post('/api/start-chat', async (req, res) => {
    try {
        const sessionId = Date.now().toString(); // 간단한 세션 ID 생성
        const chat = model.startChat({
            history: [],
            generationConfig: {
                maxOutputTokens: 1000,
            },
        });
        
        chatSessions.set(sessionId, chat);
        
        res.json({ 
            success: true, 
            sessionId: sessionId,
            message: "새로운 채팅 세션이 시작되었습니다!" 
        });
    } catch (error) {
        console.error('채팅 세션 시작 오류:', error);
        res.status(500).json({ 
            success: false, 
            error: '채팅 세션을 시작할 수 없습니다.' 
        });
    }
});

// 메시지 전송 및 응답 받기
app.post('/api/send-message', async (req, res) => {
    try {
        const { sessionId, message } = req.body;
        
        if (!sessionId || !message) {
            return res.status(400).json({ 
                success: false, 
                error: '세션 ID와 메시지가 필요합니다.' 
            });
        }
        
        const chat = chatSessions.get(sessionId);
        if (!chat) {
            return res.status(404).json({ 
                success: false, 
                error: '유효하지 않은 세션 ID입니다.' 
            });
        }
        
        const result = await chat.sendMessage(message);
        const response = await result.response;
        const text = response.text();
        
        res.json({ 
            success: true, 
            response: text 
        });
        
    } catch (error) {
        console.error('메시지 전송 오류:', error);
        res.status(500).json({ 
            success: false, 
            error: '메시지를 처리할 수 없습니다.' 
        });
    }
});

// 채팅 세션 종료
app.delete('/api/end-chat/:sessionId', (req, res) => {
    const { sessionId } = req.params;
    
    if (chatSessions.has(sessionId)) {
        chatSessions.delete(sessionId);
        res.json({ 
            success: true, 
            message: '채팅 세션이 종료되었습니다.' 
        });
    } else {
        res.status(404).json({ 
            success: false, 
            error: '유효하지 않은 세션 ID입니다.' 
        });
    }
});

// 서버 시작
app.listen(PORT, () => {
    console.log(`서버가 http://localhost:${PORT} 에서 실행 중입니다.`);
    console.log('GOOGLE_API_KEY가 설정되어 있는지 확인하세요.');
});