# This file contains a simple HelloWorldAgent.

import uuid  # สำหรับสร้าง ID ที่ไม่ซ้ำกัน

from a2a.server.agent_execution.agent_executor import AgentExecutor  # คลาสหลักสำหรับ Agent
from a2a.server.context import RequestContext  # ข้อมูลเกี่ยวกับคำขอปัจจุบัน
from a2a.server.events.event_queue import EventQueue  # คิวสำหรับส่งอีเวนต์
from a2a.types import (  # ประเภทข้อมูลต่างๆ ที่ใช้ในระบบ
    Message,
    MessageEvent,
    MessagePart,
    MessageRole,
    TaskState,
    TaskStatusUpdateEvent,
)


class HelloWorldAgent(AgentExecutor):  # HelloWorldAgent สืบทอดมาจาก AgentExecutor
    """
    เอเจนต์ง่ายๆ ที่ตอบกลับด้วยคำว่า "สวัสดี" ตามด้วยอินพุตของผู้ใช้
    """

    async def execute(
        self, context: RequestContext, event_queue: EventQueue
    ) -> None:
        """
        เมธอดหลักในการทำงานของเอเจนต์
        รับอินพุตจากผู้ใช้ สร้างข้อความตอบกลับ และส่งอีเวนต์ข้อความ
        """
        user_input = await context.get_user_input()  # รับอินพุตจากผู้ใช้

        response_string = f"สวัสดี, {user_input}!"  # สร้างข้อความตอบกลับ

        # สร้างออบเจ็กต์ Message สำหรับการตอบกลับ
        response_message = Message(
            id=str(uuid.uuid4()),  # สร้าง ID ที่ไม่ซ้ำกันสำหรับข้อความ
            role=MessageRole.ASSISTANT,  # ระบุว่าข้อความนี้มาจากผู้ช่วย
            content=[MessagePart(text=response_string)],  # เนื้อหาของข้อความ
            task_id=context.task_id,  # ID ของงานปัจจุบัน
            context_id=context.context_id,  # ID ของบริบทปัจจุบัน
        )

        # สร้าง MessageEvent จาก Message ที่สร้างขึ้น
        message_event = MessageEvent(message=response_message)
        await event_queue.put(message_event)  # ส่งอีเวนต์ข้อความไปยังคิว

        # สร้าง TaskStatusUpdateEvent เพื่อระบุว่างานเสร็จสมบูรณ์
        task_complete_event = TaskStatusUpdateEvent(
            task_id=context.task_id, status=TaskState.COMPLETED
        )
        await event_queue.put(task_complete_event)  # ส่งอีเวนต์การอัปเดตสถานะงาน

    async def cancel(
        self, context: RequestContext, event_queue: EventQueue
    ) -> None:
        """
        เมธอดสำหรับยกเลิกการทำงานของเอเจนต์
        สร้างและส่งอีเวนต์ TaskStatusUpdateEvent เพื่อระบุว่างานถูกยกเลิก
        """
        # สร้าง TaskStatusUpdateEvent เพื่อระบุว่างานถูกยกเลิก
        task_cancel_event = TaskStatusUpdateEvent(
            task_id=context.task_id, status=TaskState.CANCELED
        )
        await event_queue.put(task_cancel_event)  # ส่งอีเวนต์การอัปเดตสถานะงาน
