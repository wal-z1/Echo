import { useState, useEffect, useRef } from "react";

export default function Chatroom({ room, user }) {
	const [messages, setMessages] = useState([]);
	const [currentMessage, setCurrentMessage] = useState("");

	const socket = useRef(null);

	useEffect(() => {
		// Create the connection
		const ws = new WebSocket(`ws://127.0.0.1:1000/ws/${room}/${user}`);

		// Listen for incoming messages
		ws.onmessage = (event) => {
			setMessages((prevMessages) => [...prevMessages, event.data]);
		};

		// WebSocket object in the ref
		socket.current = ws;

		// Cleanup
		return () => {
			ws.close();
		};
	}, [room, user]); // Re-run if room or user changes

	const sendMessage = () => {
		if (currentMessage && socket.current) {
			socket.current.send(currentMessage);
			setCurrentMessage(""); // Clear input
		}
	};

	return (
		<div className="mx-auto my-auto w-full max-w-3xl bg-white/10 backdrop-blur-md border border-white/20 rounded-3xl shadow-2xl p-6 text-white">
			<div className="flex flex-col h-[560px]">
				<div className="pb-4 border-b border-white/20 mb-4 flex items-start justify-between gap-4">
					<div>
						<h2 className="font-mozilla text-2xl tracking-wide">
							Room: <span className="font-outfit font-semibold">{room}</span>
						</h2>
						<p className="text-sm text-white/70 mt-1">
							Signed in as{" "}
							<span className="font-semibold text-white">{user}</span>
						</p>
					</div>
					<div className="px-3 py-1 rounded-full border border-white/30 text-xs uppercase tracking-widest text-white/80">
						Live
					</div>
				</div>

				<div className="flex-1 overflow-y-auto space-y-3 pr-2 scrollbar-thin scrollbar-thumb-white/30 scrollbar-track-transparent">
					{messages.length === 0 && (
						<div className="h-full grid place-items-center text-center text-white/70">
							<div>
								<p className="font-mozilla text-lg">Start the conversation</p>
								<p className="text-sm mt-1">Your first message appears here.</p>
							</div>
						</div>
					)}
					{messages.map((msg, index) => (
						<div
							key={index}
							className="bg-white/15 border border-white/20 p-3 rounded-2xl shadow-sm">
							{msg}
						</div>
					))}
				</div>

				<div className="mt-4 flex items-center gap-3">
					<input
						value={currentMessage}
						onChange={(e) => setCurrentMessage(e.target.value)}
						onKeyDown={(e) => e.key === "Enter" && sendMessage()}
						type="text"
						placeholder="Type a message..."
						className="flex-1 bg-white/10 border border-white/20 rounded-xl px-4 py-3 text-sm text-white placeholder-white/60 focus:outline-none focus:ring-2 focus:ring-cyan-300"
					/>
					<button
						onClick={sendMessage}
						className="bg-cyan-400/90 hover:bg-cyan-300 text-slate-900 px-5 py-3 rounded-xl font-semibold transition">
						Send
					</button>
				</div>
			</div>
		</div>
	);
}
