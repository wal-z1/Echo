import { BrowserRouter, Routes, Route, useParams } from "react-router-dom";
import Chatroom from "./Chatroom";

function ChatroomWrapper() {
	const { room, user } = useParams();
	return <Chatroom room={room} user={user} />;
}

export default function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route
					path="/chat/:room/:user"
					element={
						<>
							<ChatroomWrapper />
						</>
					}
				/>
			</Routes>
		</BrowserRouter>
	);
}
