import { useState, useEffect } from "react";

export default function Chatroom() {
	return (
		<div className="w-full max-w-2xl bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl shadow-xl p-6 text-white">
			<div className="flex flex-col h-[500px]">
				{/*Header */}
				<div className="pb-4 border-b border-white/20 mb-4 flex items-center justify-between">
					<h2 className="text-xl font-semibold">💬 Chatroom</h2>
				</div>

				{/* Messages Area */}
				<div className="flex-1 overflow-y-auto space-y-3 p-2 scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-transparent">
					{/*include message here*/}
				</div>

				{/* Input Bar */}
				<div className="mt-4 flex items-center gap-2">
					<input
						type="text"
						placeholder="Type a message..."
						className="flex-1 bg-white/10 border border-white/20 rounded-md px-3 py-2 text-sm text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-400"
					/>
					<button className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md font-medium transition">
						Send
					</button>
				</div>
			</div>
		</div>
	);
}
